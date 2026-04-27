"""
normalize_sections.py
---------------------
Normaliza las secciones comunes del Anexo en todos los documentos
del framework.

Operaciones:
  1. Normaliza el nombre de la sección principal:
       - "## Anexo. Notas de Coworking"
         → "## Anexo. Notas de Coworking (IA Assistant)"
       - "## Anexo. Criterios de Uso"
         → "## Anexo. Criterios de Uso (IA Assisted)"

  2. Normaliza nombres de subsecciones con variantes conocidas:
       - "### Contexto adicional"      → "### Contexto"
       - "### Instrucciones para el asistente IA" → "### Instrucciones"
       - "### Riesgos identificados"   → "### Riesgos"

  3. Añade subsecciones canónicas faltantes al final del bloque
     "## Anexo. Notas de Coworking (IA Assistant)":
       ### Contexto
       ### Instrucciones
       ### Inputs utilizados
       ### Insights clave
       ### Riesgos
       ### Dudas abiertas

     Las subsecciones específicas de un documento
     (### Supuestos, ### Historial de cambios de planificación, etc.)
     no se tocan.

Uso:
  python tools/normalize_sections.py [--dry-run] [--docs-dir PATH]

Opciones:
  --dry-run   Muestra los cambios sin aplicarlos
  --docs-dir  Ruta al directorio docs/ (por defecto: docs/ relativo al script)
"""

import argparse
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────
# Configuración canónica
# ─────────────────────────────────────────────

# Nombre canónico de las secciones principales
SECTION_COWORKING_CANONICAL = "## Anexo. Notas de Coworking (IA Assistant)"
SECTION_CRITERIOS_CANONICAL = "## Anexo. Criterios de Uso (IA Assisted)"

# Variantes conocidas → nombre canónico
SECTION_RENAMES: dict[str, str] = {
    # Secciones principales
    "## Anexo. Notas de Coworking":         SECTION_COWORKING_CANONICAL,
    "## Anexo. Criterios de Uso":           SECTION_CRITERIOS_CANONICAL,
    # Subsecciones
    "### Contexto adicional":               "### Contexto",
    "### Instrucciones para el asistente IA": "### Instrucciones",
    "### Riesgos identificados":            "### Riesgos",
}

# Subsecciones canónicas del Anexo Notas de Coworking (en orden)
CANONICAL_SUBSECTIONS: list[str] = [
    "### Contexto",
    "### Instrucciones",
    "### Inputs utilizados",
    "### Insights clave",
    "### Riesgos",
    "### Dudas abiertas",
]

# Subsecciones específicas que no se propagan ni se tocan
SPECIFIC_SUBSECTIONS: set[str] = {
    "### Supuestos",
    "### Historial de cambios de planificación",
}

# Contenido vacío para subsecciones añadidas
EMPTY_SUBSECTION_BODY = "\n- ...\n"


# ─────────────────────────────────────────────
# Normalización de nombres
# ─────────────────────────────────────────────

def normalize_section_names(content: str) -> tuple[str, list[str]]:
    """
    Aplica los renombrados de SECTION_RENAMES línea a línea.
    Devuelve el contenido modificado y la lista de cambios realizados.
    """
    lines = content.splitlines(keepends=True)
    changes = []

    for i, line in enumerate(lines):
        stripped = line.rstrip("\n").rstrip()
        if stripped in SECTION_RENAMES:
            canonical = SECTION_RENAMES[stripped]
            lines[i] = line.replace(stripped, canonical, 1)
            changes.append(f"     ~ línea {i+1}: '{stripped}' → '{canonical}'")

    return "".join(lines), changes


# ─────────────────────────────────────────────
# Detección y adición de subsecciones faltantes
# ─────────────────────────────────────────────

def find_coworking_block(lines: list[str]) -> tuple[int, int]:
    """
    Localiza el bloque del Anexo Notas de Coworking.
    Devuelve (start_idx, end_idx) donde:
      - start_idx: línea del encabezado ## Anexo. Notas de Coworking
      - end_idx: primera línea de la siguiente sección ## (o fin de archivo)
    Devuelve (-1, -1) si no existe.
    """
    start = -1
    for i, line in enumerate(lines):
        if line.rstrip() == SECTION_COWORKING_CANONICAL:
            start = i
            break

    if start == -1:
        return -1, -1

    # Buscar el siguiente ## (que no sea ###)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## ") and not lines[i].startswith("### "):
            return start, i

    return start, len(lines)


def get_existing_subsections(lines: list[str], start: int, end: int) -> list[str]:
    """Extrae los nombres de las subsecciones ### dentro del bloque."""
    subs = []
    for line in lines[start:end]:
        stripped = line.rstrip()
        if stripped.startswith("### "):
            subs.append(stripped)
    return subs


def add_missing_subsections(
    lines: list[str],
    start: int,
    end: int,
    existing: list[str],
) -> tuple[list[str], list[str]]:
    """
    Añade al final del bloque las subsecciones canónicas que faltan.
    No toca las subsecciones específicas ni reordena las existentes.
    Devuelve las líneas modificadas y la lista de subsecciones añadidas.
    """
    missing = [s for s in CANONICAL_SUBSECTIONS if s not in existing]
    if not missing:
        return lines, []

    # Insertar antes de end (o al final del archivo)
    insertion = []
    for sub in missing:
        insertion.append("\n")
        insertion.append(f"{sub}\n")
        insertion.append(f"{EMPTY_SUBSECTION_BODY}\n")

    # Buscar el último carácter no vacío antes de end para insertar limpiamente
    insert_at = end
    for i in range(end - 1, start, -1):
        if lines[i].strip():
            insert_at = i + 1
            break

    new_lines = lines[:insert_at] + insertion + lines[insert_at:]
    return new_lines, missing


# ─────────────────────────────────────────────
# Procesamiento de un documento
# ─────────────────────────────────────────────

def process_document(
    path: Path,
    dry_run: bool,
) -> tuple[bool, list[str]]:
    """
    Procesa un documento aplicando normalización de nombres
    y adición de subsecciones faltantes.

    Devuelve (changed, list_of_changes).
    """
    content = path.read_text(encoding="utf-8")
    all_changes = []

    # 1. Normalizar nombres de secciones
    content, name_changes = normalize_section_names(content)
    all_changes.extend(name_changes)

    # 2. Añadir subsecciones faltantes
    lines = content.splitlines(keepends=True)
    start, end = find_coworking_block(lines)

    if start != -1:
        existing = get_existing_subsections(lines, start, end)
        lines, added = add_missing_subsections(lines, start, end, existing)
        for sub in added:
            all_changes.append(f"     + añadida: '{sub}'")
        content = "".join(lines)

    if not all_changes:
        return False, []

    if not dry_run:
        path.write_text(content, encoding="utf-8")

    return True, all_changes


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normaliza secciones comunes del Anexo en los documentos del framework."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Muestra los cambios sin aplicarlos.")
    parser.add_argument("--docs-dir", type=Path,
                        default=Path(__file__).parent.parent / "docs",
                        help="Ruta al directorio docs/.")
    args = parser.parse_args()

    docs_dir = args.docs_dir.resolve()
    if not docs_dir.exists():
        print(f"❌ Directorio no encontrado: {docs_dir}")
        sys.exit(1)

    mode = "DRY RUN" if args.dry_run else "APLICANDO CAMBIOS"
    print(f"\n{'─' * 54}")
    print(f"  normalize_sections.py — {mode}")
    print(f"  docs/: {docs_dir}")
    print(f"{'─' * 54}\n")
    print(f"  Sección canónica : {SECTION_COWORKING_CANONICAL}")
    print(f"  Subsecciones     : {', '.join(s.lstrip('# ') for s in CANONICAL_SUBSECTIONS)}")
    print(f"\n{'─' * 54}\n")

    md_files = sorted(docs_dir.rglob("*.md"))
    changed_count = 0

    for md_file in md_files:
        rel = str(md_file.relative_to(docs_dir))
        if rel == "00_INDEX.md":
            continue

        changed, changes = process_document(md_file, args.dry_run)
        prefix = "🔍" if (args.dry_run and changed) else ("✅" if changed else " ")
        print(f"  {prefix} {rel}")
        for change in changes:
            print(change)
        if changed:
            changed_count += 1
            print()

    print(f"\n{'─' * 54}")
    status_word = "con cambios detectados" if args.dry_run else "modificados"
    print(f"  Documentos {status_word}: {changed_count} / {len(md_files) - 1}")
    print(f"{'─' * 54}\n")


if __name__ == "__main__":
    main()

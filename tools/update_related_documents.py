"""
update_related_documents.py
---------------------------
Actualiza el campo related_documents del frontmatter de cada documento
del framework según el mapa declarativo definido en docs/00_INDEX.md.

El mapa en 00_INDEX.md es la fuente de verdad de las referencias.
Cualquier discrepancia entre el mapa y el contenido de los archivos
es tratada como un problema a corregir.

Uso:
  python tools/update_related_documents.py [--dry-run] [--docs-dir PATH] [--validate-only]

Opciones:
  --dry-run        Muestra los cambios sin aplicarlos
  --docs-dir       Ruta al directorio docs/ (por defecto: docs/ relativo al script)
  --validate-only  Solo valida sin proponer cambios
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


# ─────────────────────────────────────────────
# Lectura del mapa desde 00_INDEX.md
# ─────────────────────────────────────────────

def load_reference_map(docs_dir: Path) -> dict[str, list[str]]:
    """
    Extrae el bloque YAML de la sección 'Mapa de Referencias'
    del archivo 00_INDEX.md y lo devuelve como diccionario.
    """
    index_path = docs_dir / "00_INDEX.md"
    if not index_path.exists():
        raise FileNotFoundError(f"No se encontró 00_INDEX.md en: {docs_dir}")

    content = index_path.read_text(encoding="utf-8")

    pattern = re.compile(
        r"#[^\n]*Mapa de Referencias[^\n]*\n.*?```yaml\n(.*?)```",
        re.DOTALL,
    )
    match = pattern.search(content)
    if not match:
        raise ValueError(
            "No se encontró el bloque YAML en la sección 'Mapa de Referencias' de 00_INDEX.md."
        )

    data = yaml.safe_load(match.group(1))

    if not isinstance(data, dict) or "reference_map" not in data:
        raise ValueError(
            "El bloque YAML en 00_INDEX.md debe contener la clave 'reference_map'."
        )

    return data["reference_map"]


# ─────────────────────────────────────────────
# Frontmatter helpers
# ─────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[list[str], str, bool]:
    """
    Extrae el frontmatter de un documento Markdown.
    Devuelve (fm_lines, body, has_frontmatter).
    """
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return [], content, False

    fm_lines = []
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break
        fm_lines.append(line)

    if end_idx is None:
        return [], content, False

    body = "".join(lines[end_idx + 1:])
    return fm_lines, body, True


def get_current_refs(fm_lines: list[str]) -> list[str]:
    """Extrae las referencias actuales de related_documents."""
    refs = []
    in_related = False
    for line in fm_lines:
        stripped = line.strip()
        if stripped == "related_documents:":
            in_related = True
            continue
        if in_related:
            if stripped.startswith("- "):
                refs.append(stripped[2:].strip())
            elif stripped:
                in_related = False
    return refs


def build_frontmatter(fm_lines: list[str], new_refs: list[str]) -> str:
    """
    Reconstruye el bloque frontmatter reemplazando related_documents
    por new_refs. Si no existe la clave, la añade al final.
    """
    result = []
    in_related = False
    related_written = False

    for line in fm_lines:
        stripped = line.strip()

        if stripped == "related_documents:":
            in_related = True
            related_written = True
            result.append("related_documents:\n")
            for ref in new_refs:
                result.append(f"  - {ref}\n")
            continue

        if in_related:
            if stripped.startswith("- "):
                continue
            else:
                in_related = False

        result.append(line)

    if not related_written:
        result.append("related_documents:\n")
        for ref in new_refs:
            result.append(f"  - {ref}\n")

    return "---\n" + "".join(result) + "---\n"


# ─────────────────────────────────────────────
# Validación
# ─────────────────────────────────────────────

def validate_map(reference_map: dict[str, list[str]], docs_dir: Path) -> list[str]:
    """
    Valida el mapa declarativo contra el filesystem.
    """
    issues = []

    for doc, refs in reference_map.items():
        if not (docs_dir / doc).exists():
            issues.append(f"❌ Documento en mapa no encontrado en disco: {doc}")
        for ref in refs:
            if not (docs_dir / ref).exists():
                issues.append(f"❌ Referencia inexistente en mapa [{doc}]: {ref}")

    for md_file in sorted(docs_dir.rglob("*.md")):
        rel = str(md_file.relative_to(docs_dir))
        if rel == "00_INDEX.md":
            continue
        if rel not in reference_map:
            issues.append(f"⚠️  Documento en disco no cubierto por el mapa: {rel}")

    return issues


def validate_references_on_disk(docs_dir: Path) -> list[str]:
    """Detecta referencias rotas o placeholders en los frontmatters."""
    issues = []
    for md_file in sorted(docs_dir.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        fm_lines, _, has_fm = parse_frontmatter(content)
        if not has_fm:
            continue
        rel = str(md_file.relative_to(docs_dir))
        for ref in get_current_refs(fm_lines):
            if ref.startswith("["):
                issues.append(f"⚠️  Placeholder sin resolver en {rel}: {ref}")
            elif not (docs_dir / ref).exists():
                issues.append(f"❌ Referencia rota en {rel}: {ref}")
    return issues


# ─────────────────────────────────────────────
# Procesamiento de documentos
# ─────────────────────────────────────────────

def process_document(
    doc_rel: str,
    expected_refs: list[str],
    docs_dir: Path,
    dry_run: bool,
) -> tuple[bool, str]:
    """
    Compara las referencias actuales con las esperadas y aplica el fix.
    """
    path = docs_dir / doc_rel
    if not path.exists():
        return False, "⚠️  Archivo no encontrado en disco — omitido"

    content = path.read_text(encoding="utf-8")
    fm_lines, body, has_fm = parse_frontmatter(content)

    if not has_fm:
        return False, "⚠️  Sin frontmatter — omitido"

    current_refs = get_current_refs(fm_lines)

    if current_refs == expected_refs:
        return False, "✓  Sin cambios"

    added = [r for r in expected_refs if r not in current_refs]
    removed = [r for r in current_refs if r not in expected_refs]
    reordered = not added and not removed and current_refs != expected_refs

    if not dry_run:
        new_fm = build_frontmatter(fm_lines, expected_refs)
        path.write_text(new_fm + body, encoding="utf-8")

    lines = []
    for r in added:
        lines.append(f"     + {r}")
    for r in removed:
        lines.append(f"     - {r}")
    if reordered:
        lines.append("     ~ reordenadas")

    return True, "\n".join(lines)


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Actualiza related_documents según el mapa en docs/00_INDEX.md."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Muestra los cambios sin aplicarlos.")
    parser.add_argument("--docs-dir", type=Path,
                        default=Path(__file__).parent.parent / "docs",
                        help="Ruta al directorio docs/.")
    parser.add_argument("--validate-only", action="store_true",
                        help="Solo valida el mapa y referencias en disco.")
    args = parser.parse_args()

    docs_dir = args.docs_dir.resolve()
    if not docs_dir.exists():
        print(f"❌ Directorio no encontrado: {docs_dir}")
        sys.exit(1)

    mode = "VALIDACIÓN" if args.validate_only else ("DRY RUN" if args.dry_run else "APLICANDO CAMBIOS")
    print(f"\n{'─' * 54}")
    print(f"  update_related_documents.py — {mode}")
    print(f"  docs/: {docs_dir}")
    print(f"{'─' * 54}\n")

    # ── Cargar mapa ──────────────────────────────────────
    try:
        reference_map = load_reference_map(docs_dir)
        print(f"  ✅ Mapa cargado desde 00_INDEX.md ({len(reference_map)} documentos)\n")
    except (FileNotFoundError, ValueError) as e:
        print(f"  ❌ Error al cargar el mapa: {e}")
        sys.exit(1)

    # ── Validación del mapa ──────────────────────────────
    print("Validando mapa declarativo...\n")
    map_issues = validate_map(reference_map, docs_dir)
    if map_issues:
        print("  Problemas en el mapa:")
        for issue in map_issues:
            print(f"  {issue}")
        print()
        if args.validate_only:
            sys.exit(1)
    else:
        print("  ✅ Mapa válido — todos los documentos y referencias existen.\n")

    if args.validate_only:
        print("Validando referencias actuales en disco...\n")
        disk_issues = validate_references_on_disk(docs_dir)
        if disk_issues:
            for issue in disk_issues:
                print(f"  {issue}")
        else:
            print("  ✅ Todas las referencias en disco son válidas.")
        print(f"\n{'─' * 54}\n")
        return

    # ── Procesamiento ────────────────────────────────────
    print(f"{'─' * 54}")
    print("  Actualizando related_documents...\n")

    changed_count = 0
    for doc_rel, expected_refs in reference_map.items():
        changed, status = process_document(doc_rel, expected_refs, docs_dir, args.dry_run)
        prefix = "🔍" if (args.dry_run and changed) else ("✅" if changed else " ")
        print(f"  {prefix} {doc_rel}")
        if changed:
            print(status)
            changed_count += 1
        print()

    # ── Validación post-aplicación ───────────────────────
    print(f"{'─' * 54}")
    print("  Validando referencias en disco tras los cambios...\n")
    disk_issues = validate_references_on_disk(docs_dir)
    if disk_issues:
        print("  Problemas encontrados:")
        for issue in disk_issues:
            print(f"  {issue}")
    else:
        print("  ✅ Todas las referencias en disco son válidas.")

    print(f"\n{'─' * 54}")
    status_word = "con cambios detectados" if args.dry_run else "actualizados"
    print(f"  Documentos {status_word}: {changed_count} / {len(reference_map)}")
    print(f"{'─' * 54}\n")


if __name__ == "__main__":
    main()

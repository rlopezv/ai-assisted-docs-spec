"""
update_index.py
---------------
Regenera las secciones dinámicas de docs/00_INDEX.md:

  1. Tabla de estado — lee el campo `status` del frontmatter de cada
     documento del mapa y actualiza la tabla '📊 Estado de las Plantillas'.

  2. Diagrama Mermaid — genera un diagrama classDiagram donde cada capa
     es una clase con sus documentos como atributos, y las flechas entre
     clases representan las dependencias entre capas derivadas del mapa.

Ambas secciones son regeneradas completamente en cada ejecución.
El resto del contenido de 00_INDEX.md no se modifica.

Uso:
  python tools/update_index.py [--dry-run] [--docs-dir PATH]

Opciones:
  --dry-run   Muestra el resultado sin escribir el archivo
  --docs-dir  Ruta al directorio docs/ (por defecto: docs/ relativo al script)
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


# ─────────────────────────────────────────────
# Configuración de capas
#
# Define el nombre de display de cada capa y el prefijo de ruta
# que identifica los documentos que pertenecen a ella.
# El orden determina el orden en la tabla y en el diagrama.
# ─────────────────────────────────────────────

LAYERS: list[dict] = [
    {"name": "Business",     "prefix": "business/",            "emoji": "📋"},
    {"name": "Data",         "prefix": "data/",                "emoji": "🗄️"},
    {"name": "Architecture", "prefix": "architecture/",        "emoji": "🏗️"},
    {"name": "API",          "prefix": "api/",                 "emoji": "🔌"},
    {"name": "LLM",          "prefix": "llm/",                 "emoji": "🤖"},
    {"name": "QA",           "prefix": "qa/",                  "emoji": "✅"},
    {"name": "Operations",   "prefix": "operations/",          "emoji": "⚙️"},
]

# Emojis para cada estado en la tabla
STATUS_EMOJI: dict[str, str] = {
    "not_started": "⚪",
    "draft":       "🔵",
    "review":      "🟡",
    "done":        "🟢",
}

# Texto de display para cada estado
STATUS_LABEL: dict[str, str] = {
    "not_started": "No iniciado",
    "draft":       "Draft",
    "review":      "En revisión",
    "done":        "Completado",
}


# ─────────────────────────────────────────────
# Lectura del mapa desde 00_INDEX.md
# ─────────────────────────────────────────────

def load_reference_map(docs_dir: Path) -> dict[str, list[str]]:
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
        raise ValueError("El bloque YAML debe contener la clave 'reference_map'.")

    return data["reference_map"]


# ─────────────────────────────────────────────
# Lectura de frontmatter
# ─────────────────────────────────────────────

def read_status(doc_path: Path) -> str:
    """
    Lee el campo `status` del frontmatter de un documento.
    Devuelve el valor normalizado a minúsculas con guiones bajos.
    Si el archivo no existe devuelve 'not_started'.
    Si el valor no está entre los estados conocidos devuelve 'draft'.
    """
    KNOWN_STATUSES = {"not_started", "draft", "review", "done"}

    if not doc_path.exists():
        return "not_started"

    content = doc_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return "draft"

    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("status:"):
            raw = line.split(":", 1)[1].strip().lower()
            normalized = raw.replace(" ", "_").replace("-", "_")
            return normalized if normalized in KNOWN_STATUSES else "draft"

    return "draft"


# ─────────────────────────────────────────────
# Generación de la tabla de estado
# ─────────────────────────────────────────────

def generate_status_table(
    reference_map: dict[str, list[str]],
    docs_dir: Path,
) -> str:
    """
    Genera la tabla Markdown de estado de las plantillas
    agrupada por capa.
    """
    rows = []
    rows.append("| Área | Documento | Estado | Notas |")
    rows.append("| ---- | --------- | ------ | ----- |")

    for layer in LAYERS:
        layer_docs = [
            doc for doc in reference_map
            if doc.startswith(layer["prefix"])
        ]
        layer_docs.sort()

        for doc in layer_docs:
            status_key = read_status(docs_dir / doc)
            emoji = STATUS_EMOJI.get(status_key, "⚪")
            label = STATUS_LABEL.get(status_key, status_key)
            filename = Path(doc).name
            # Incluir subdirectorio si es template
            parent = Path(doc).parent
            display = (
                f"{parent.name}/{filename}"
                if parent.name not in ("business", "data", "architecture", "api", "llm", "qa", "operations")
                else filename
            )
            rows.append(f"| {layer['name']} | {display} | {emoji} {label} | |")

    return "\n".join(rows)


# ─────────────────────────────────────────────
# Generación del diagrama Mermaid
# ─────────────────────────────────────────────

def layer_of(doc: str) -> str | None:
    """Devuelve el nombre de la capa a la que pertenece un documento."""
    for layer in LAYERS:
        if doc.startswith(layer["prefix"]):
            return layer["name"]
    return None


def doc_label(doc: str) -> str:
    """Nombre corto del documento para usar como atributo en el diagrama."""
    name = Path(doc).stem  # sin extensión
    # Si está en templates/, prefijamos con templates/
    parts = Path(doc).parts
    if "templates" in parts:
        return f"templates/{name}"
    return name


def generate_mermaid(reference_map: dict[str, list[str]]) -> str:
    """
    Genera un diagrama classDiagram Mermaid donde:
    - cada capa es una clase
    - los documentos de la capa son atributos
    - las flechas entre clases representan dependencias entre capas
    """
    lines = []
    lines.append("```mermaid")
    lines.append("classDiagram")

    # ── Clases (una por capa) ────────────────────────────
    for layer in LAYERS:
        layer_docs = sorted(
            doc for doc in reference_map
            if doc.startswith(layer["prefix"])
        )
        lines.append(f"    class {layer['name']} {{")
        for doc in layer_docs:
            lines.append(f"        {doc_label(doc)}")
        lines.append("    }")

    lines.append("")

    # ── Relaciones entre capas ───────────────────────────
    # Una flecha entre capas A → B si algún doc de A referencia algún doc de B
    # y A ≠ B. Se deduplican.
    layer_deps: set[tuple[str, str]] = set()

    for doc, refs in reference_map.items():
        src_layer = layer_of(doc)
        if src_layer is None:
            continue
        for ref in refs:
            tgt_layer = layer_of(ref)
            if tgt_layer is None or tgt_layer == src_layer:
                continue
            layer_deps.add((src_layer, tgt_layer))

    # Ordenar para output determinista
    for src, tgt in sorted(layer_deps):
        lines.append(f"    {src} --> {tgt}")

    lines.append("```")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# Actualización de 00_INDEX.md
# ─────────────────────────────────────────────

# Marcadores que delimitan las secciones regeneradas
MARKER_STATUS_START = "<!-- STATUS_TABLE_START -->"
MARKER_STATUS_END   = "<!-- STATUS_TABLE_END -->"
MARKER_MERMAID_START = "<!-- MERMAID_START -->"
MARKER_MERMAID_END   = "<!-- MERMAID_END -->"


def inject_section(
    content: str,
    marker_start: str,
    marker_end: str,
    new_content: str,
) -> tuple[str, bool]:
    """
    Reemplaza el contenido entre marker_start y marker_end.
    Si los marcadores no existen, devuelve el contenido original sin cambios
    e indica que no se pudo inyectar.
    """
    pattern = re.compile(
        re.escape(marker_start) + r".*?" + re.escape(marker_end),
        re.DOTALL,
    )
    replacement = f"{marker_start}\n{new_content}\n{marker_end}"
    new, count = pattern.subn(replacement, content)
    return new, count > 0


def ensure_markers(content: str) -> str:
    """
    Si el INDEX no tiene los marcadores, los inserta en las posiciones
    correctas (alrededor de la tabla de estado y al final antes de los
    principios de uso).
    """
    # Marcadores de tabla de estado
    if MARKER_STATUS_START not in content:
        status_header = "# 📊 Estado de las Plantillas"
        if status_header in content:
            # Insertar marcadores alrededor del bloque de tabla existente
            # Buscamos la tabla (líneas que empiezan con |) tras el header
            pattern = re.compile(
                r"(" + re.escape(status_header) + r"\n\n)((?:\|[^\n]*\n)+)",
                re.DOTALL,
            )
            def add_markers(m):
                return (
                    m.group(1)
                    + MARKER_STATUS_START + "\n"
                    + m.group(2).rstrip("\n") + "\n"
                    + MARKER_STATUS_END + "\n"
                )
            content = pattern.sub(add_markers, content)
        else:
            # Añadir la sección completa antes de Principios de uso
            insertion = (
                f"# 📊 Estado de las Plantillas\n\n"
                f"{MARKER_STATUS_START}\n"
                f"{MARKER_STATUS_END}\n\n---\n\n"
            )
            target = "# 🧭 Principios de uso"
            content = content.replace(target, insertion + target, 1)

    # Marcadores de Mermaid
    if MARKER_MERMAID_START not in content:
        mermaid_header = "# 🗺️ Mapa de Referencias"
        if mermaid_header in content:
            # Insertar bloque Mermaid justo antes del bloque yaml existente
            pattern = re.compile(
                r"(" + re.escape(mermaid_header) + r".*?)(```yaml)",
                re.DOTALL,
            )
            def add_mermaid_markers(m):
                return (
                    m.group(1)
                    + MARKER_MERMAID_START + "\n"
                    + MARKER_MERMAID_END + "\n\n"
                    + m.group(2)
                )
            content = pattern.sub(add_mermaid_markers, content, count=1)

    return content


def update_index(
    docs_dir: Path,
    reference_map: dict[str, list[str]],
    dry_run: bool,
) -> None:
    index_path = docs_dir / "00_INDEX.md"
    content = index_path.read_text(encoding="utf-8")

    # Asegurar que los marcadores existen
    content = ensure_markers(content)

    # Generar contenido nuevo
    status_table = generate_status_table(reference_map, docs_dir)
    mermaid = generate_mermaid(reference_map)

    # Inyectar tabla de estado
    content, ok_status = inject_section(
        content, MARKER_STATUS_START, MARKER_STATUS_END, status_table
    )
    if not ok_status:
        print("  ⚠️  No se pudo inyectar la tabla de estado.")

    # Inyectar Mermaid
    content, ok_mermaid = inject_section(
        content, MARKER_MERMAID_START, MARKER_MERMAID_END, mermaid
    )
    if not ok_mermaid:
        print("  ⚠️  No se pudo inyectar el diagrama Mermaid.")

    if dry_run:
        print("\n── Tabla de estado generada ──────────────────────────\n")
        print(status_table)
        print("\n── Diagrama Mermaid generado ─────────────────────────\n")
        print(mermaid)
    else:
        index_path.write_text(content, encoding="utf-8")
        print("  ✅ 00_INDEX.md actualizado.")


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regenera tabla de estado y diagrama Mermaid en docs/00_INDEX.md."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Muestra el resultado sin escribir el archivo.")
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
    print(f"  update_index.py — {mode}")
    print(f"  docs/: {docs_dir}")
    print(f"{'─' * 54}\n")

    try:
        reference_map = load_reference_map(docs_dir)
        print(f"  ✅ Mapa cargado desde 00_INDEX.md ({len(reference_map)} documentos)\n")
    except (FileNotFoundError, ValueError) as e:
        print(f"  ❌ Error al cargar el mapa: {e}")
        sys.exit(1)

    update_index(docs_dir, reference_map, args.dry_run)

    print(f"\n{'─' * 54}\n")


if __name__ == "__main__":
    main()

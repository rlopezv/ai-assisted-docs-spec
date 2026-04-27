"""
fix_frontmatter.py
------------------
Corrige problemas estructurales en el frontmatter de los documentos del framework.

Fixes incluidos:
  1. Typo en PRD: business/01_projet_brief.md → business/01_project_brief.md
  2. Auto-referencia en Prompt Library: llm/02_prompt_library.md → llm/01_llm_integration_spec.md
  3. Línea espuria en Operational Spec: línea en blanco entre --- y document:
  4. Placeholder en Domain Model: [Documentos relevantes del proyecto] → referencias reales
  5. Placeholder en Data Dictionary: [Documentos relevantes del proyecto] → referencias reales
  6. Architecture Overview: añadir architecture/02_technical_design.md a related_documents

Uso:
  python tools/fix_frontmatter.py [--dry-run] [--docs-dir PATH]

Opciones:
  --dry-run     Muestra los cambios sin aplicarlos
  --docs-dir    Ruta al directorio docs/ (por defecto: docs/ relativo al script)
"""

import argparse
import re
import sys
from pathlib import Path


# ─────────────────────────────────────────────
# Configuración de fixes
# ─────────────────────────────────────────────

FIXES = [
    {
        "id": "PRD-typo",
        "description": "Typo en related_documents del PRD: 'projet' → 'project'",
        "file": "business/02_prd.md",
        "type": "replace",
        "old": "  - business/01_projet_brief.md",
        "new": "  - business/01_project_brief.md",
    },
    {
        "id": "prompt-library-self-ref",
        "description": "Auto-referencia en Prompt Library: sustituir por llm/01_llm_integration_spec.md",
        "file": "llm/02_prompt_library.md",
        "type": "replace",
        "old": "  - llm/02_prompt_library.md",
        "new": "  - llm/01_llm_integration_spec.md",
    },
    {
        "id": "operational-spec-blank-line",
        "description": "Línea en blanco espuria tras el primer '---' en Operational Spec",
        "file": "operations/01_operational_spec.md",
        "type": "replace",
        "old": "---\n\ndocument:",
        "new": "---\ndocument:",
    },
    {
        "id": "domain-model-placeholder",
        "description": "Placeholder en related_documents de Domain Model → referencias reales",
        "file": "data/01_domain_model.md",
        "type": "replace",
        "old": "  - [Documentos relevantes del proyecto]",
        "new": (
            "  - business/01_project_brief.md\n"
            "  - business/02_prd.md\n"
            "  - data/02_data_dictionary.md"
        ),
    },
    {
        "id": "data-dictionary-placeholder",
        "description": "Placeholder en related_documents de Data Dictionary → referencias reales",
        "file": "data/02_data_dictionary.md",
        "type": "replace",
        "old": "  - [Documentos relevantes del proyecto]",
        "new": (
            "  - business/02_prd.md\n"
            "  - data/01_domain_model.md"
        ),
    },
    {
        "id": "architecture-overview-missing-ref",
        "description": "Añadir architecture/02_technical_design.md a related_documents de Architecture Overview",
        "file": "architecture/01_architecture_overview.md",
        "type": "insert_after",
        "after": "  - business/02_prd.md",
        "insert": "  - architecture/02_technical_design.md",
        "only_in_frontmatter": True,
    },
]


# ─────────────────────────────────────────────
# Utilidades
# ─────────────────────────────────────────────

def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def extract_frontmatter_end(content: str) -> int:
    """Devuelve el índice del cierre del frontmatter (segundo ---)."""
    lines = content.split("\n")
    count = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            count += 1
            if count == 2:
                return i
    return -1


def apply_replace(content: str, old: str, new: str) -> tuple[str, bool]:
    if old not in content:
        return content, False
    return content.replace(old, new, 1), True


def apply_insert_after(
    content: str, after: str, insert: str, only_in_frontmatter: bool
) -> tuple[str, bool]:
    """Inserta 'insert' en la línea siguiente a 'after'.
    Si only_in_frontmatter, solo opera dentro del bloque frontmatter.
    """
    lines = content.split("\n")
    fm_end = extract_frontmatter_end(content) if only_in_frontmatter else len(lines)

    for i, line in enumerate(lines):
        if only_in_frontmatter and i > fm_end:
            break
        if line.rstrip() == after:
            # Comprobar que ya no existe el valor a insertar
            if insert in lines:
                return content, False
            lines.insert(i + 1, insert)
            return "\n".join(lines), True

    return content, False


# ─────────────────────────────────────────────
# Aplicación de fixes
# ─────────────────────────────────────────────

def apply_fix(fix: dict, docs_dir: Path, dry_run: bool) -> bool:
    path = docs_dir / fix["file"]

    if not path.exists():
        print(f"  ⚠️  Archivo no encontrado: {fix['file']}")
        return False

    content = read_file(path)
    original = content

    if fix["type"] == "replace":
        content, changed = apply_replace(content, fix["old"], fix["new"])

    elif fix["type"] == "insert_after":
        content, changed = apply_insert_after(
            content,
            fix["after"],
            fix["insert"],
            fix.get("only_in_frontmatter", False),
        )

    else:
        print(f"  ⚠️  Tipo de fix desconocido: {fix['type']}")
        return False

    if not changed:
        print(f"  ℹ️  Sin cambios (ya correcto o patrón no encontrado): {fix['file']}")
        return False

    if dry_run:
        print(f"  🔍 [DRY RUN] Cambio detectado en: {fix['file']}")
        _print_diff(original, content)
    else:
        write_file(path, content)
        print(f"  ✅ Aplicado: {fix['file']}")

    return True


def _print_diff(original: str, modified: str) -> None:
    orig_lines = original.splitlines()
    mod_lines = modified.splitlines()

    removed = set(orig_lines) - set(mod_lines)
    added = set(mod_lines) - set(orig_lines)

    for line in orig_lines:
        if line in removed:
            print(f"     - {line}")
    for line in mod_lines:
        if line in added:
            print(f"     + {line}")


# ─────────────────────────────────────────────
# Validación post-fix
# ─────────────────────────────────────────────

def validate_references(docs_dir: Path) -> list[str]:
    """Verifica que todas las related_documents apuntan a archivos existentes."""
    errors = []
    md_files = sorted(docs_dir.rglob("*.md"))

    for md_file in md_files:
        content = read_file(md_file)
        fm_end = extract_frontmatter_end(content)
        if fm_end == -1:
            continue

        fm_lines = content.split("\n")[: fm_end + 1]
        in_related = False

        for line in fm_lines:
            if "related_documents:" in line:
                in_related = True
                continue
            if in_related:
                stripped = line.strip()
                if stripped.startswith("- "):
                    ref = stripped[2:].strip()
                    if ref.startswith("["):
                        errors.append(
                            f"  ⚠️  Placeholder sin resolver en {md_file.relative_to(docs_dir)}: {ref}"
                        )
                    else:
                        target = docs_dir / ref
                        if not target.exists():
                            errors.append(
                                f"  ❌ Referencia rota en {md_file.relative_to(docs_dir)}: {ref}"
                            )
                elif stripped and not stripped.startswith("-"):
                    in_related = False

    return errors


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Corrige problemas estructurales en el frontmatter del framework."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra los cambios sin aplicarlos.",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path(__file__).parent.parent / "docs",
        help="Ruta al directorio docs/ (por defecto: ../docs relativo al script).",
    )
    args = parser.parse_args()

    docs_dir = args.docs_dir.resolve()

    if not docs_dir.exists():
        print(f"❌ Directorio no encontrado: {docs_dir}")
        sys.exit(1)

    mode = "DRY RUN" if args.dry_run else "APLICANDO CAMBIOS"
    print(f"\n{'─' * 50}")
    print(f"  fix_frontmatter.py — {mode}")
    print(f"  docs/: {docs_dir}")
    print(f"{'─' * 50}\n")

    applied = 0
    for fix in FIXES:
        print(f"[{fix['id']}] {fix['description']}")
        if apply_fix(fix, docs_dir, args.dry_run):
            applied += 1
        print()

    # Validación post-fix
    print(f"{'─' * 50}")
    print("  Validando referencias cruzadas...\n")
    errors = validate_references(docs_dir)

    if errors:
        print("  Problemas encontrados:")
        for e in errors:
            print(e)
    else:
        print("  ✅ Todas las referencias son válidas.")

    print(f"\n{'─' * 50}")
    status = "simulados" if args.dry_run else "aplicados"
    print(f"  Fixes {status}: {applied} / {len(FIXES)}")
    print(f"{'─' * 50}\n")


if __name__ == "__main__":
    main()

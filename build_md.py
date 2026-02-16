"""Convert all Markdown files in md_pages/ into Django templates."""

from pathlib import Path

import markdown


MD_DIR = Path("./md_pages")
TEMPLATE_DIR = Path("./templates")


def discover_pages() -> list[str]:
    """Return page names (relative to md_pages/, without .md extension).

    e.g. ["index", "healthcare", "bills_federal/gerrymandering", ...]
    """
    return sorted(
        p.relative_to(MD_DIR).with_suffix("").as_posix() for p in MD_DIR.rglob("*.md")
    )


def build_markdown() -> None:
    pages = discover_pages()

    for page in pages:
        md_text = (MD_DIR / f"{page}.md").read_text(encoding="utf-8")
        html = markdown.markdown(md_text, extensions=["extra", "toc", "codehilite"])

        template_text = (
            '{% extends "base.html" %}\n'
            "{% load static %}\n"
            "\n"
            "{% block contents %}\n"
            f"{html}\n"
            "{% endblock %}\n"
        )

        out_path = TEMPLATE_DIR / f"{page}.html"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(template_text, encoding="utf-8")
        print(f"  {page}.md -> templates/{page}.html")

    print(f"\nDone. {len(pages)} templates written.")


if __name__ == "__main__":
    build_markdown()

from pathlib import Path

import markdown

from main_.views import pages

def build_markdown() -> None:
    for page in pages:
        md_text = Path(f"./md_pages/{page}.md").read_text(encoding="utf-8")
        html = markdown.markdown(md_text, extensions=["extra", "toc", "codehilite"])

        template_text = f"""{{% extends "base.html" %}}
{{% load static %}}

{{% block contents %}}
{html}
{{% endblock %}}
"""

        print("TT: {:?}", template_text)

        Path(f"./templates/{page}.html").write_text(template_text, encoding="utf-8")


build_markdown()
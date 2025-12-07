from pathlib import Path

import markdown
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def compile_markdown() -> None:
    """Compiles all relevant markdown files to HTML"""

    md_files = [
        "introduction",
        "heathcare",
        "election_reformeducation",
        "veterans",
        "infrastructure",
        "healthcare",
        "environment",
    ]

    for f in md_files:
        md_text = Path(f"{f}.md").read_text(encoding="utf-8")
        html = markdown.markdown(md_text, extensions=["extra", "toc", "codehilite"])

        Path(f"{f}.html").write_text(html, encoding="utf-8")


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})


def bills(request: HttpRequest) -> HttpResponse:
    return render(request, "bills.html", {})


def education(request: HttpRequest) -> HttpResponse:
    return render(request, "education.html", {})


def election_reform(request: HttpRequest) -> HttpResponse:
    return render(request, "election_reform.html", {})


def environment(request: HttpRequest) -> HttpResponse:
    return render(request, "environment.html", {})


def housing(request: HttpRequest) -> HttpResponse:
    return render(request, "housing.html", {})


def infrastructure(request: HttpRequest) -> HttpResponse:
    return render(request, "infrastructure.html", {})


def veterans(request: HttpRequest) -> HttpResponse:
    return render(request, "veterans.html", {})

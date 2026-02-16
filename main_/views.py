from pathlib import Path

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

MD_DIR = Path(__file__).resolve().parent.parent / "md_pages"


def _discover_pages() -> set[str]:
    """Build the page whitelist by scanning md_pages/."""
    return {
        str(p.relative_to(MD_DIR).with_suffix("")).replace("\\", "/")
        for p in MD_DIR.rglob("*.md")
    }


pages = _discover_pages()


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})


def page_generic(request: HttpRequest, page: str) -> HttpResponse:
    if page not in pages:
        raise Http404()
    return render(request, f"{page}.html", {})

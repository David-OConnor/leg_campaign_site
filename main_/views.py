from pathlib import Path

from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

# Must match the markdown names. Used to create HTML files,
# urls, and views.
pages = [
    # "introduction",
    "healthcare",
    "election_reform",
    "education",
    "veterans",
    "infrastructure",
    "healthcare",
    "environment",
]

# def build_markdown() -> None:
#     for page in pages:
#         md_text = Path(f"{page}.md").read_text(encoding="utf-8")
#         html = markdown.markdown(md_text, extensions=["extra", "toc", "codehilite"])
#
#         template_text = f"""{{% extends "base.html" %}}
# {{% load static %}}
#
# {{% block contents %}}
# {html}
# {{% endblock %}}
# """
#
#         Path(f"templates/{page}.html").write_text(template_text, encoding="utf-8")


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index_old.html", {})


def page_generic(request: HttpRequest, page: str) -> HttpResponse:
    if page not in pages:
        raise Http404()
    return render(request, f"{page}.html", {})

# def bills(request: HttpRequest) -> HttpResponse:
#     return render(request, "bills.html", {})
#
#
# def education(request: HttpRequest) -> HttpResponse:
#     return render(request, "education.html", {})
#
#
# def election_reform(request: HttpRequest) -> HttpResponse:
#     return render(request, "election_reform.html", {})
#
#
# def environment(request: HttpRequest) -> HttpResponse:
#     return render(request, "environment.html", {})
#
#
# def housing(request: HttpRequest) -> HttpResponse:
#     return render(request, "housing.html", {})
#
#
# def infrastructure(request: HttpRequest) -> HttpResponse:
#     return render(request, "infrastructure.html", {})
#
#
# def veterans(request: HttpRequest) -> HttpResponse:
#     return render(request, "veterans.html", {})

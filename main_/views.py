from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

# Must match the markdown names. Used to create HTML files,
# urls, and views.
pages = [
    "index",
    "healthcare",
    "election_reform",
    "education",
    "veterans",
    "infrastructure",
    "healthcare",
    "environment",
]


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})


def page_generic(request: HttpRequest, page: str) -> HttpResponse:
    if page not in pages:
        raise Http404()
    return render(request, f"{page}.html", {})

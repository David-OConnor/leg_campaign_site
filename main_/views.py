from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", {})


def bills(request: HttpRequest) -> HttpResponse:
    return render(request, "bills.html", {})


def education(request: HttpRequest) -> HttpResponse:
    return render(request, "education.html", {})


def election_reform(request: HttpRequest) -> HttpResponse:
    return render(request, "election_reform.html", {})


def housing(request: HttpRequest) -> HttpResponse:
    return render(request, "housing.html", {})


def infrastructure(request: HttpRequest) -> HttpResponse:
    return render(request, "infrastructure.html", {})

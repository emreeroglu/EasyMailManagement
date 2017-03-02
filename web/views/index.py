from django.shortcuts import render


def index(request):
    """Index Page."""
    return render(request, "web/index.html", {})

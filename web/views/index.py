from django.shortcuts import render
from fabfile import install_sudo
from server.models import Server


def index(request):
    """Index Page."""
    return render(request, "web/index.html", {})

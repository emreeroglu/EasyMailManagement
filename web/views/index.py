from django.shortcuts import render
from fabfile import install_sudo

def index(request):
    """Index Page."""
    install_sudo()
    return render(request, "web/index.html", {})

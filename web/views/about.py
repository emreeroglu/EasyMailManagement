from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def about(request):
    return render(request, "web/about.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def contact(request):
    return render(request, "web/contact.html")

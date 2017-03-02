from django.shortcuts import render
from web.forms import RegisterForm


def register_page(request):
    form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})

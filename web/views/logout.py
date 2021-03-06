from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('index')

from django.contrib.auth import login
from django.shortcuts import render, redirect

from common.forms import RegisterForm


def register_page(request):
    if request.user.is_authenticated:
        # User is already logged in, redirect to index
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            # @TODO Use confirmation sms !! make email optional
            login(request, user)
            return redirect('index')
        # form is not valid:
        return render(request, 'web/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})

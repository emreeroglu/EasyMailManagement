from django.contrib.auth import login
from django.shortcuts import render, redirect

from common.forms import RegisterForm
from django.contrib.auth.hashers import make_password


def register_page(request):
    if request.user.is_authenticated:
        # User is already logged in, redirect to index
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(password=form.cleaned_data['password'])
            user.save()
            # @TODO Use confirmation sms !! make email area optional
            login(request, user)
            return redirect('index')
        # for is not valid:
        return render(request, 'web/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})

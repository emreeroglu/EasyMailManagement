from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from common.models import User
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
        # form is not valid:
        return render(request, 'web/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})


def check_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = _('A user with this username already exists.')
    return JsonResponse(data)

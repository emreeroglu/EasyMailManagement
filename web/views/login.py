from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from web.forms import LoginForm
from common.models import User


def get_user(email=None, username=None):
    try:
        if email:
            return User.objects.get(email=email.lower())
        else:
            return User.objects.get(username=username.lower())
    except User.DoesNotExist:
        return None


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url = request.POST['next']
        user = get_user(username=username)
        if user.is_authenticated():
            return redirect('index')
        if not username or not password:
            return render(request, 'web/login.html', {'error': _('Missing Fields')})
        if '@' in username:
            _user = get_user(email=username)
        else:
            _user = get_user(username=username)
        if not _user:
            return render(request, 'web/login.html', {'error': _('User not found')})
        username = _user.username
        _user = authenticate(username=username, password=password)
        if _user:
            if _user.is_active:
                login(request, _user)
                return redirect(next_url)
            else:
                return render(request, 'web/login.html', {'error': _('Account Disabled')})
        else:
            return render(request, 'web/login.html', {'error': _('Invalid login credentials')})

    form = LoginForm()
    return render(request, 'web/login.html', {'form': form})
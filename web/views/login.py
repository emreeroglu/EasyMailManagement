from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from common.forms import LoginForm
from common.models import User


def get_user(email=None, username=None):
    try:
        if email:
            return User.objects.get(email=email.lower())
        else:
            return User.objects.get(username=username.lower())
    except User.DoesNotExist:
        return None


# @TODO: check username in template with ajax
def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        next_url = request.POST.get('next', None)
        # Check if all required information supplied or not
        if not username or not password:
            return render(request, 'web/login.html', {'form': form, 'error': _('Missing Fields.')})
        # Check user existence.
        user = get_user(username=username)
        if not user:
            return render(request, 'web/login.html', {'form': form, 'error': _('User not found.')})
        # Check is user authenticated or not.
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(next_url)
            else:
                return render(request, 'web/login.html', {'form': form, 'error': _('Account Disabled.')})
        else:
            return render(request, 'web/login.html', {'form': form, 'error': _('Invalid login credentials.')})
    return render(request, 'web/login.html', {'form': form})

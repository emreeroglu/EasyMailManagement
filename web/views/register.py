from common.models import User
from django.shortcuts import render, redirect
from web.forms import RegisterForm
from django.contrib.auth import authenticate


def register_page(request):
    form = RegisterForm()
    return render(request, 'web/register.html', {'form': form})


def doregister(request):
    if request.method == 'POST':
        if request.user.is_anonymous:
            request_form = request.POST['form']
            if request_form is not None:
                form = RegisterForm(request.form)
                if request.method == 'POST' and form.validate():
                    # @TODO Check if user with same email or username exists
                    user = User(
                        first_name=form.first_name,
                        last_name=form.last_name,
                        username=form.username,
                        email=form.email,
                        mobile=form.mobile,
                        language=form.language,
                    )
                    user = user.save()
                    # @TODO Use confirmation email
                    user = authenticate(user.username, user.password)
                    if user is not None:
                        return redirect('index')
                    else:
                        clean_form = RegisterForm()
                        return redirect('register_page', {'form': clean_form})
        elif request.user.is_authenticated:
            return redirect('index')
    return redirect('index')

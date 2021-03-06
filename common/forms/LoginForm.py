from django.utils.translation import ugettext_lazy as _
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q


class LoginForm(forms.ModelForm):
    """Create login form."""
    username = forms.CharField(
        label=_("Username"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )
    password = forms.CharField(
        label=_("Password"),
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': _('Password'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

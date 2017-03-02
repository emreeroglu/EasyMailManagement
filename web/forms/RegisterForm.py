from django.utils.translation import ugettext_lazy as _
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class RegisterForm(forms.ModelForm):
    """Create register form."""
    first_name = forms.CharField(
        label=_("First Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('First Name'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last Name'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )
    mobile = forms.CharField(
        label=_("Mobile Phone"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('+'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control phone-number',
            'type': 'tel',
            'required': 'required'
        })
    )
    language = forms.ChoiceField(
        label=_("Preferred Language"),
        required=True,
        choices=settings.LANGUAGES,
        initial='en',
        widget=forms.Select(attrs={
            'class': 'form-control select2'
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'mobile', 'language']

    def clean_email(self):
        """
        Avoid multiple email addresses
        :return: str email
        """
        email = self.cleaned_data.get('email')
        if not self.instance.pk and email:
            try:
                get_user_model().objects.get(email=email)
                raise ValidationError(_("This email address is already registered."))
            except get_user_model().DoesNotExist:
                # No user with such email, its ok to create new one
                pass
        return email

class EditRegisterForm(RegisterForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'mobile', 'language']
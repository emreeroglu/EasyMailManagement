from django.utils.translation import ugettext_lazy as _
from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from collections import OrderedDict


class RegisterForm(forms.ModelForm):
    """Create register form."""
    first_name = forms.CharField(
        label=_("First Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('First Name'),
            'class': 'form-control',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Last Name'),
            'class': 'form-control',
            'required': 'required'
        })
    )
    username = forms.CharField(
        label=_("Username"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Username'),
            'class': 'form-control',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': _('Email'),
            'class': 'form-control',
            'required': 'required'
        })
    )
    mobile = forms.CharField(
        label=_("Mobile Phone"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('+'),
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
    password = forms.CharField(
        label=_("Password"),
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'placeholder': _("Password")
        })
    )
    password_confirm = forms.CharField(
        label=_("Confirm Password"),
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'required': 'required',
            'placeholder': _("Enter password again to confirm")
        })
    )

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'mobile', 'language']

    def __init__(self,*args,**kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # import code
        # code.interact(local=locals())
        fields_keyOrder = ['first_name', 'last_name', 'username', 'email', 'password', 'password_confirm',
                           'mobile', 'language']
        self.fields = OrderedDict((k, self.fields[k]) for k in fields_keyOrder)

    def clean(self):
        password = self.cleaned_data.get('password', '')
        password_confirm = self.cleaned_data.get('password_confirm', '')
        if password != password_confirm:
            raise forms.ValidationError(_("Password doesn't match"))

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

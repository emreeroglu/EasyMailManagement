from django.utils.translation import ugettext_lazy as _
from django import forms
from electronicmail.models import ElectronicMail


class AddElectronicMailForm(forms.ModelForm):
    email = forms.EmailField(
        label=_("Full Email Address"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('EMail Address'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )
    mail_box_size = forms.IntegerField(
        label=_("Size Of Mailbox (as mb)"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('10'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

    class Meta:
        model = ElectronicMail
        fields = ['email', 'mail_box_size']

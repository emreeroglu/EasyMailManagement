from django.utils.translation import ugettext_lazy as _
from django import forms
from server.models import Server


class AddServerForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Server Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Server Name'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

    static_mailbox_quota = forms.IntegerField(
        label=_("Static Mailbox Quota"),
        widget=forms.TextInput(attrs={
            'placeholder': _('0'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

    is_for_sell = forms.BooleanField(
        label=_("Is For Sell"),
        widget=forms.CheckboxInput(attrs={
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

    class Meta:
        model = Server
        fields = ['name']

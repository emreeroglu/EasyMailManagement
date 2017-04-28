from django.utils.translation import ugettext_lazy as _
from django import forms
from server.models import Server


class AddServerForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Server Name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Server Name'),
            'class': 'form-control',
            'required': 'required'
        })
    )

    static_mailbox_quota = forms.IntegerField(
        label=_("Static Mailbox Quota"),
        initial='0',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'required': 'required'
        })
    )

    is_for_sell = forms.BooleanField(
        label=_("Is For Sell"),
        required=False
    )

    class Meta:
        model = Server
        fields = ['name']

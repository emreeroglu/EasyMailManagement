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

    class Meta:
        model = Server
        fields = ['name']

from django import forms


class AddServerFrom(forms.ModelForm):
    name = forms.CharField(
        label=_("name"),
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': _('Server Name'),
            'oninvalid': 'makeFormActive();',
            'class': 'form-control',
            'required': 'required'
        })
    )

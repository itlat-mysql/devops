from django import forms
from django.utils.translation import gettext as _


class ContactsForm(forms.Form):
    email = forms.EmailField(label=_('Email'), max_length=255)
    content = forms.CharField(label=_('Question'), max_length=1000)

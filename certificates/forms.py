from django import forms
from .models import certificate


class cert_verify(forms.Form):
    id = forms.UUIDField()

form = cert_verify()
from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contact


class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation

    def __init__(self, *args, **kwargs):
        return super(ContactForm, self).__init__(*args, **kwargs)

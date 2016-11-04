from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import DateField
from contacts.models import Contact


class CitationForm(forms.Form):
	user = forms.ForeignKey(User)
    author_fname = forms.CharField(max_length = 128)
    author_lname = forms.CharField(max_length = 128)
    title = forms.CharField(max_length = 256)
    link = forms.CharField(max_length = 1024)
    notes = forms.CharField(max_length = 65536)
    date_pub = forms.DateField()
    date_acc = forms.DateField()
    






    #class Meta:
        #model = Citation

    #def __init__(self, *args, **kwargs):
        #return super(ContactForm, self).__init__(*args, **kwargs)

from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import DateField
from .models import Citation
from django.forms import ModelForm



class CitationForm(forms.ModelForm):
	class Meta:
		model = Citation
		fields = ("author_fname", "author_lname", "title", "link", "date_acc", "date_pub", "notes",)
	
    






    #class Meta:
        #model = Citation

    #def __init__(self, *args, **kwargs):
        #return super(ContactForm, self).__init__(*args, **kwargs)

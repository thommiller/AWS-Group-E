from django.db import models
from django import forms
from django.forms.fields import DateField
from django.contrib.auth.models import User

DATE_FORMATS = ['%d/%m/%Y',]

class Citation(models.Model):
    user = models.ForeignKey(User)
    author_fname = models.CharField(max_length = 128, default = '0000000')
    author_lname = models.CharField(max_length = 128, default = '0000000')
    title = models.CharField(max_length = 256, default = '0000000')
    link = models.CharField(max_length = 1024, default = '0000000')
    notes = models.CharField(max_length = 65536, default = '0000000')
    date_pub = models.DateField(default="1970-01-01")
    date_acc = models.DateField(default="1970-01-01")

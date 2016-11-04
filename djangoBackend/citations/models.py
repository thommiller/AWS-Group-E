from django.db import models
from django import forms
from django.forms.fields import DateField
from django.contrib.auth.models import User

DATE_FORMATS = ['%d/%m/%Y',]

class Citation(models.Model):
    user = models.ForeignKey(User)
    author_fname = models.CharField(max_length = 128, default = '')
    author_lname = models.CharField(max_length = 128, default = '')
    title = models.CharField(max_length = 256, default = '')
    link = models.CharField(max_length = 1024, default = '')
    notes = models.CharField(max_length = 65536, default = '')
    date_pub = models.DateField(default="2000-01-01")
    date_acc = models.DateField(default="2000-01-01")

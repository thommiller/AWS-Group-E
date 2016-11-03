from django.db import models
from django import forms
from django.forms.fields import DateField


DATE_FORMATS = ['%d/%m/%Y',]


class User(models.Model):
    name = models.CharField(max_length = 32)
    passwordHash = models.CharField(max_length = 1024)

class Citation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    author = models.CharField(max_length = 256, default = '0000000')
    title = models.CharField(max_length = 256, default = '0000000')
    link = models.CharField(max_length = 1024, default = '0000000')
    notes = models.CharField(max_length = 65536, default = '0000000')
    date_pub = models.DateField(default="1970-01-01")
    date_acc = models.DateField(default="1970-01-01")

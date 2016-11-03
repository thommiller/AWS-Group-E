from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 32)
    passwordHash = models.CharField(max_length = 1024)

class Citation(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    link = models.CharField(max_length = 1024)
    note = models.CharField(max_length = 65536, default = '')
from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100, default=None)
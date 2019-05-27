from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    url = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

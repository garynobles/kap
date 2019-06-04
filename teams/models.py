from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class TeamMembers(models.Model):
    team_member =  models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT)
    team = models.CharField(max_length=50, default='', blank=True, null=True)
    role = models.CharField(max_length=50, default='', blank=True, null=True)

class Team(models.Model):
    team_name = models.CharField(max_length=200, default='', blank=True, null=True)

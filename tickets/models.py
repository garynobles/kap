from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CAT_CHOICES = (
    ("option","option"),
    ("other","other")
)

DEPT_CHOICES = (
    ("Zooarch","Zooarchaeology"),
    ("other","other")
)

TICKET_STATUS_CHOICES = (
    ("awaiting assignment","awaiting assignment"),
    ("assigned","assigned"),
    ("resolved","resolved")
)

# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT)
    subject = models.CharField(max_length=200, default='', blank=True, null=True)
    details = models.CharField(max_length=5000, default='', blank=True, null=True)
    category = models.CharField(max_length=20, default='', choices = CAT_CHOICES)
    department = models.CharField(max_length=20, default='', choices = DEPT_CHOICES)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='assigned_to', blank=True, null=True, on_delete = models.PROTECT, related_name='assigned')
    status = models.CharField(max_length=20, default='', choices = TICKET_STATUS_CHOICES)
    datetime = models.DateTimeField(auto_now_add=True)

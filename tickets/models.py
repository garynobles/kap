from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CAT_CHOICES = (
    ("option","option"),
    ("general request","general request"),
    ("other","other"),
)

DEPT_CHOICES = (
    ("3D Spatial", "3D Spatial"),
    ("Botany","Botany"),
    ("Ceramics","Ceramics"),
    ("Conservation","Conservation"),
    ("Database","Database"),
    ("Excavation","Excavation"),
    ("Zooarch","Zooarchaeology"),
    ("Other","Other")
)

TICKET_STATUS_CHOICES = (
    ("awaiting assignment","awaiting assignment"),
    ("assigned","assigned"),
    ("completed","completed")
)

SYS_CHOICES = (
    ("MS Database","MS Database"),
    ("Website","Website"),
    ("GIS","GIS"),
    ("other","other"),
)

PRIORITY_CHOICES = (
    ("Urgent","Urgent (Hour)"),
    ("High","High (Day)"),
    ("Medium","Medium (Week)"),
    ("Low","Low (Season)"),
    ("None","None")
)
# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT)
    subject = models.CharField(max_length=200, default='')
    details = models.CharField(max_length=5000, default='')
    category = models.CharField(max_length=20, default='', choices = CAT_CHOICES)
    system = models.CharField(max_length=20, default='', choices = SYS_CHOICES)
    department = models.CharField(max_length=20, default='', choices = DEPT_CHOICES, blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='assigned_to', blank=True, null=True, on_delete = models.PROTECT, related_name='assigned')
    status = models.CharField(max_length=20, default='awaiting assignment', blank=True, null=True, choices = TICKET_STATUS_CHOICES)
    priority = models.CharField(max_length=20, default='', blank=True, null=True, choices = PRIORITY_CHOICES)
    datetime = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

CAT_CHOICES = (
    ("option","option"),
    ("menu change","menu change"),
    ("new form","new form"),
    ("form alteration","form alteration"),
    ("general request","general request"),
    ("sample delete","sample delete"),
    ("other","other"),
)

DEPT_CHOICES = (
    ("3D Spatial", "3D Spatial"),
    ("Botany","Botany"),
    ("Ceramics","Ceramics"),
    ("Conservation","Conservation"),
    ("Database","Database"),
    ("Excavation","Excavation"),
    ("Small Finds","Small Finds"),
    ("Website","Website"),
    ("Zooarch","Zooarchaeology"),
    ("Other","Other"),
)

TICKET_STATUS_CHOICES = (
    ("awaiting assignment","awaiting assignment"),
    ("assigned","assigned"),
    ("next migration","next migration"),
    ("completed","completed"),
    ("clarification requested","clarification requested"),
)

SYS_CHOICES = (
    ("MS Access Forms","MS Access Forms"),
    ("Web Aesthetics","Web Aesthetics"),
    ("Web Functionality","Web Functionality"),
    ("GIS","GIS"),
    ("Non-system","Non-system"),
    ("other","other"),
)

PRIORITY_CHOICES = (
    ("Urgent","Urgent (Hour)"),
    ("High","High (Day)"),
    ("Medium","Medium (Week)"),
    ("Low","Low (Season)"),
    ("None","None"),
)
# Create your models here.
class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, blank=True, null=True)
    subject = models.CharField(max_length=200, default='')
    details = models.CharField(max_length=5000, default='')
    category = models.CharField(max_length=30, default='', choices = CAT_CHOICES)
    system = models.CharField(max_length=30, default='', choices = SYS_CHOICES)
    department = models.CharField(max_length=30, default='', choices = DEPT_CHOICES, blank=True, null=True)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT, related_name='assigned')
    status = models.CharField(max_length=30, default='awaiting assignment', blank=True, null=True, choices = TICKET_STATUS_CHOICES)
    priority = models.CharField(max_length=30, default='', blank=True, null=True, choices = PRIORITY_CHOICES)
    datetime = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = 'public\".\"tickets_ticket_old'
    #     #ordering = ["sample_id"]
    #     managed = False
    #     #verbose_name_plural = "samples"

    # def __str__(self):
    #     return '{} {}'.format(
    #         self.assigned_to.first_name,
    #         self.assigned_to.last_name
    #     )

    # def __str__(self):
        # return self.taken_by.first_name
        # return str(self.sample_id)
        # return str(self.firstname)+ '-' +str(self.lastname)
        # return u'%s %s' % (assigned_to.first_name, self.last_name)
        # return str(self.user.first_name)
        # return str(self.location_name)+ '.' +str(self.location_sub_name)
    # class Meta:
        # ordering = ["-priority"]

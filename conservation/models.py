from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
from botany.choices import EASTING_CHOICES, NORTHING_CHOICES, RECOVERY_METHODS, MATERIALS

class Sample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField(choices = EASTING_CHOICES)
    area_northing = models.IntegerField(choices = NORTHING_CHOICES)
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    # material_type = models.CharField(max_length=200, default='', blank=True, null=True, choices = MATERIALS)
    sample_type = models.CharField(max_length=200, default='', blank=True, null=True, choices = MATERIALS)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    recovery_method = models.CharField(max_length=200, default='', blank=True, null=True, choices = RECOVERY_METHODS)
    taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT, related_name='taken_by')
    # taken_by = models.ForeignKey(public.auth_user, db_column='taken_by', on_delete = models.PROTECT)
    comments = models.CharField(max_length=1000, default='', blank=True, null=True)

    def __str__(self):
        # return self.taken_by.first_name
        return str(self.sample_id)
        # return str(self.firstname)+ '-' +str(self.lastname)
        # return u'%s %s' % (self.first_name, self.last_name)


    class Meta:
        db_table = 'kap\".\"sample'
        ordering = ["sample_id"]
        managed = False
        #verbose_name_plural = "samples"


class Condition(models.Model):
    conservation_id =  models.AutoField(primary_key=True)
    sample_id = models.ForeignKey(Sample, db_column='sample_id', on_delete = models.PROTECT)
    conservation_number = models.IntegerField()
    deterioration_assessment = models.CharField(max_length=600, default='', blank=True, null=True)
    fragment_count = models.IntegerField()
    start_date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    structure = models.CharField(max_length=600, default='', blank=True, null=True)
    surface = models.CharField(max_length=600, default='', blank=True, null=True)

    def __str__(self):
        # return self.taken_by.first_name
        return str(self.conservation_number)
        # return str(self.firstname)+ '-' +str(self.lastname)
        # return u'%s %s' % (self.first_name, self.last_name)


    class Meta:
        db_table = 'kap\".\"conservation_condition'
        # ordering = ["sample_id"]
        managed = False
        #verbose_name_plural = "samples"

#
#
# class Observation(models.Model):
#
#     def __str__(self):
#         # return self.taken_by.first_name
#         return str(self.sample_id)
#         # return str(self.firstname)+ '-' +str(self.lastname)
#         # return u'%s %s' % (self.first_name, self.last_name)
#
#
#     class Meta:
#         db_table = 'kap\".\"sample'
#         ordering = ["sample_id"]
#         managed = False
#         #verbose_name_plural = "samples"
#
#
#
# class Materials(models.Model):
#
#
#         def __str__(self):
#             # return self.taken_by.first_name
#             return str(self.sample_id)
#             # return str(self.firstname)+ '-' +str(self.lastname)
#             # return u'%s %s' % (self.first_name, self.last_name)
#
#
#         class Meta:
#             db_table = 'kap\".\"sample'
#             ordering = ["sample_id"]
#             managed = False
#             #verbose_name_plural = "samples"
#
# class Treatment(models.Model):
#
#
#         def __str__(self):
#             # return self.taken_by.first_name
#             return str(self.sample_id)
#             # return str(self.firstname)+ '-' +str(self.lastname)
#             # return u'%s %s' % (self.first_name, self.last_name)
#
#
#         class Meta:
#             db_table = 'kap\".\"sample'
#             ordering = ["sample_id"]
#             managed = False
#             #verbose_name_plural = "samples"
#
#
#
# class Action(models.Model):
#
#
#         def __str__(self):
#             # return self.taken_by.first_name
#             return str(self.sample_id)
#             # return str(self.firstname)+ '-' +str(self.lastname)
#             # return u'%s %s' % (self.first_name, self.last_name)
#
#
#         class Meta:
#             db_table = 'kap\".\"sample'
#             ordering = ["sample_id"]
#             managed = False
#             #verbose_name_plural = "samples"

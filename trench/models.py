from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Trench(models.Model):
    trench_id = models.AutoField(primary_key=True)
    trench_name = models.CharField(max_length=500, default='', blank=True, null=True)
    area_easting = models.IntegerField()
    area_northing = models.IntegerField()

    def __str__(self):
        #return str(self.trench_name)
        return str(self.area_easting)+ '.' +str(self.area_northing)

    class Meta:
        db_table = 'kap\".\"trench'
        ordering = ["area_easting","area_northing"]
        managed = False
        verbose_name_plural = "trenches"

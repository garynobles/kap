from django.db import models

# Create your models here.
class Models3d(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=500)
    filename =models.CharField(max_length=20)

    def __str__(self):
        return self.context_number_tmp

    class Meta():
        managed=False
        db_table = 'kap\".\"models3d'
        # ordering = ["orderby"]
        verbose_name_plural = "3D Models"

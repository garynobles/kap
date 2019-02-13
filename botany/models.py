from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

EASTING_CHOICES = (
    ("",""),
    (99, 99),
    (108, 108),
    (109, 109),
    (81,81),
    (84,84),
    (93,93),
    (95,95),
    (97,97),
    (98,98),
    (987,987),

)


class Sample(models.Model):
    sample_id = models.AutoField(primary_key=True)
    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    taken_by = models.IntegerField()
    # taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.PROTECT)

    def __str__(self):
        return str(self.sample_number)

    class Meta:
        db_table = 'samples\".\"sample'
        #ordering = ["sample_id"]
        managed = False
        #verbose_name_plural = "samples"


class Botany(models.Model):
    botany_id = models.AutoField(primary_key=True)
    sample_id = models.ForeignKey(Sample, db_column='sample_id', on_delete = models.PROTECT)
    area_easting = models.IntegerField(blank=True, null=True)
    area_northing = models.IntegerField(blank=True, null=True)
    context_number = models.IntegerField(blank=True, null=True)
    sample_number = models.IntegerField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=False)
    flotation_date = models.DateTimeField(auto_now=False)
    analyst = models.CharField(max_length=200, default='', blank=True, null=True)
    notes = models.CharField(max_length=600, default='', blank=True, null=True)

    def __str__(self):
        return str(self.botany_id)

    class Meta():
        managed=False
        db_table = 'samples\".\"botany'
        #ordering = ["orderby"]
        verbose_name_plural = "Botany"


class Fraction(models.Model):
    fraction_id = models.AutoField(primary_key=True)
    botany_id = models.ForeignKey(Botany, db_column='botany_id', on_delete = models.PROTECT)
    proportion_analysed = models.DecimalField(max_digits=5, decimal_places=3)
    soil_volume = models.DecimalField(max_digits=15, decimal_places=4)
    sample_volume = models.DecimalField(max_digits=15, decimal_places=4)
    sample_weight = models.DecimalField(max_digits=15, decimal_places=4)
    sediment = models.BooleanField()
    stone = models.BooleanField()
    roots = models.BooleanField()
    leaves = models.BooleanField()
    insect_parts = models.BooleanField()
    charred_dung = models.BooleanField()
    bone = models.BooleanField()
    shell = models.BooleanField()

    def __str__(self):
        return str(self.fraction_id)

    class Meta():
        managed=False
        db_table = 'samples\".\"fraction'
        #ordering = ["orderby"]
        verbose_name_plural = "Fraction"

class FractionComposition(models.Model):
    fract_comp_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
    material_type = models.CharField(max_length=50, default='')
    fraction = models.CharField(max_length=50, default='')
    type_count = models.DecimalField(max_digits=15, decimal_places=4)
    whole_weight = models.DecimalField(max_digits=15, decimal_places=4)
    fragment_weight = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return str(self.fract_comp_id)

    class Meta():
        managed=False
        db_table = 'samples\".\"fraction_composition'
        #ordering = ["orderby"]
        verbose_name_plural = "Composition"

class FractionMaterialsPresent(models.Model):
    pass
#
#     material_id = models.AutoField(primary_key=True)
#     fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
#     # material = models.CharField(max_length=200, default='')
#
#     sediment = models.BooleanField()
#     stone = models.BooleanField()
#     roots = models.BooleanField()
#     leaves = models.BooleanField()
#     insect_parts = models.BooleanField()
#     charred_dung = models.BooleanField()
#     bone = models.BooleanField()
#     shell = models.BooleanField()
#
#     def __str__(self):
#         return str(self.material_id)
#
#     class Meta():
#         managed=False
#         db_table = 'samples\".\"materials_present'
#         #ordering = ["orderby"]
#         verbose_name_plural = "Materials Present"

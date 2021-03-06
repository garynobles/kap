from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from botany.choices import EASTING_CHOICES, NORTHING_CHOICES, RECOVERY_METHODS, MATERIALS, FRACTIONS

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
    taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT)
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


class Flotation(models.Model):
    flotation_id = models.AutoField(primary_key=True)
    sample_id = models.ForeignKey(Sample, db_column='sample_id', on_delete = models.PROTECT)
    # area_easting = models.IntegerField(choices = EASTING_CHOICES)
    # area_northing = models.IntegerField(choices = NORTHING_CHOICES)
    # context_number = models.IntegerField(blank=True, null=True)
    # sample_number = models.IntegerField(blank=True, null=True)
    flotation_date = models.DateTimeField(auto_now=False)
    entry_date = models.DateTimeField(auto_now_add=False)
    analyst_id = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='analyst_id', on_delete = models.PROTECT)
    notes = models.CharField(max_length=600, default='', blank=True, null=True)

    def __str__(self):
        return str(self.flotation_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"flotation'
        #ordering = ["orderby"]
        verbose_name_plural = "Flotation"


class LightResidue(models.Model):
    lightresidue_id = models.AutoField(primary_key=True)
    flotation_id = models.ForeignKey(Flotation, db_column='flotation_id', on_delete = models.PROTECT)
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
        return str(self.lightresidue_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"lightresidue'
        #ordering = ["orderby"]
        verbose_name_plural = "LightResidue"

class Composition(models.Model):
    composition_id = models.AutoField(primary_key=True)
    lightresidue_id = models.ForeignKey(LightResidue, db_column='lightresidue_id', on_delete = models.PROTECT)
    material_type = models.CharField(max_length=50, default='')
    type_count = models.DecimalField(max_digits=15, decimal_places=4)
    whole_weight = models.DecimalField(max_digits=15, decimal_places=4)
    fragment_weight = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return str(self.composition_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"composition'
        #ordering = ["orderby"]
        verbose_name_plural = "Composition"

class Fraction(models.Model):
    fraction_id = models.AutoField(primary_key=True)
    composition_id = models.ForeignKey(Composition, db_column='composition_id', on_delete = models.PROTECT)
    fraction = models.CharField(max_length=20, choices = FRACTIONS)
    def __str__(self):
        return str(self.fraction_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"fraction'
        #ordering = ["orderby"]
        verbose_name_plural = "Fraction"

class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    taxon = models.CharField(max_length=50, blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    species = models.CharField(max_length=50, blank=True, null=True)
    genus = models.CharField(max_length=50, blank=True, null=True)
    # family_name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.species)

    class Meta():
        managed=False
        db_table = 'kap\".\"plant_species'
        ordering = ["genus","species"]
        verbose_name_plural = "species"

class PlantPart(models.Model):
    plantpart_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
    species_id = models.ForeignKey(Species, db_column='species_id', on_delete = models.PROTECT, related_name='plant_species', blank=True, null=True)
    part = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)


    def __str__(self):
        return str(self.plantpart_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"plant_part'
        #ordering = ["orderby"]
        verbose_name_plural = "plant parts"

class Seed(models.Model):
    seed_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', blank=True, null=True, on_delete = models.PROTECT)
    species_id = models.ForeignKey(Species, db_column='species_id', blank=True, null=True, on_delete = models.PROTECT, related_name='seed_species')
    weight_type = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    quantity_type = models.CharField(max_length=50)
    quantity = models.IntegerField()


    def __str__(self):
        return str(self.seed_id)

    class Meta():
        managed=False
        db_table = 'kap\".\"seed'
        ordering = ["species_id","fraction_id"]
        verbose_name_plural = "seeds"

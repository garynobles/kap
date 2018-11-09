from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Samples(models.Model):

    #container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
    sample_id = models.IntegerField(blank=True, null=True)
    #sample_id = models.AutoField(primary_key=True)

    #container_id = models.IntegerField()

    area_easting = models.IntegerField()
    area_northing = models.IntegerField()
    context_number = models.IntegerField()
    sample_number = models.AutoField(primary_key=True)

    material = models.CharField(max_length=25)
    specific_material = models.CharField(max_length=50, blank=True, null=True)
    exterior_color_hue = models.CharField(max_length=6, blank=True, null=True)
    exterior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    exterior_color_chroma = models.IntegerField(blank=True, null=True)
    interior_color_hue = models.CharField(max_length=6, blank=True, null=True)
    interior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    interior_color_chroma = models.IntegerField(blank=True, null=True)
    weight_kilograms = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    sample_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    current_location = models.CharField(max_length=50)
    recovery_type = models.CharField(max_length=25)
    problems = models.CharField(max_length=300, blank=True, null=True)
    image_files = models.CharField(max_length=50, blank=True, null=True)
    number_3d_files = models.CharField(db_column='3d_files', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    chronology = models.CharField(max_length=100, blank=True, null=True)
    analysis_request = models.CharField(max_length=50, blank=True, null=True)
    detailed_sample_description = models.TextField(blank=True, null=True)
    bureaucratic_status = models.CharField(max_length=25, blank=True, null=True)
    subjective_significance = models.NullBooleanField()
    museum_inventory_number = models.IntegerField(blank=True, null=True)
    bureaucratic_status_identifier = models.CharField(max_length=100, blank=True, null=True)

    #VirtualField
    # necs = CompositeForeignKey(
    # #necs = CompositeOneToOneField(
    #     Container,
    #     on_delete=DO_NOTHING,
    #     #related_name='containers',
    #     related_name='samples',
    #     to_fields={
    #         "area_easting": "area_easting",
    #         "area_northing": "area_northing",
    #         "context_number": "context_number",
    #         "sample_number": "sample_number" })

    #sample_id = models.AutoField(unique=True)

    def __str__(self):
        return str(self.sample_number)

    class Meta:
        db_table = 'samples\".\"samples'
        #ordering = ["sample_id"]
        managed = False
        #verbose_name_plural = "samples"
        #unique_together = (('area_easting', 'area_northing', 'context_number', 'sample_number'),)


class Botany(models.Model):
    botany_id = models.AutoField(primary_key=True)
    sample_id = models.IntegerField(blank=True, null=True)
    #sample_id = models.ForeignKey(Samples, db_column='sample_id', on_delete = models.PROTECT)
    area_easting = models.IntegerField(blank=True, null=True)
    area_northing = models.IntegerField(blank=True, null=True)
    context_number = models.IntegerField(blank=True, null=True)
    sample_number = models.IntegerField(blank=True, null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    analysis_date = models.DateTimeField(auto_now=True)
    analyst = models.CharField(max_length=200, default='')
    notes = models.CharField(max_length=600, default='')

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

    material_id = models.AutoField(primary_key=True)
    fraction_id = models.ForeignKey(Fraction, db_column='fraction_id', on_delete = models.PROTECT)
    material = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.material_id)

    class Meta():
        managed=False
        db_table = 'samples\".\"materials_present'
        #ordering = ["orderby"]
        verbose_name_plural = "Materials Present"

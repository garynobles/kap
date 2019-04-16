from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from templates.choices import EASTING_CHOICES, NORTHING_CHOICES, RECOVERY_METHODS, MATERIALS







# class Container(models.Model): #container
#     container_name = models.CharField(max_length=50, blank=True, null=True)
#     containers = models.ManyToManyField('Sample')
#     # container_id = models.AutoField(primary_key=True)
#     # # samples = models.IntegerField()
#     # # samples = models.ManyToManyField(Sample, through='JoinSampleContainer', through_fields=('container_id', 'sample_id'), related_name='containers')
#     # samples = models.ManyToManyField(Sample, related_name='containers')
#     # location_id = models.ForeignKey(Location, db_column='location_id', on_delete = models.PROTECT)
#     # icon_desc = models.ForeignKey(Icon, db_column='icon_desc', null=True, blank=True, default='Box',on_delete = models.PROTECT)
#     # container_name = models.CharField(max_length=50, blank=True, null=True)
#     container_type = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return self.container_name
#
#     class Meta:
#         db_table = 'kap\".\"container'
#         verbose_name_plural = "container"
#
#
# class Sample(models.Model): #sample
#     sample_id = models.AutoField(primary_key=True)
#     # topping_name = models.CharField(max_length=30, default='None')
#     sample_number = models.IntegerField()
#
#     def __str__(self):
#         return str(self.sample_number)
#
#     class Meta:
#         db_table = 'kap\".\"sample'
#         verbose_name_plural = "samplex"













class Icon(models.Model):
    icon_desc = models.CharField(primary_key=True,max_length=50)
    icon = models.ImageField(upload_to='images/icons/')

    def __str__(self):
        return self.icon_desc

    class Meta:
        db_table = 'kap\".\"icon'
        #ordering = ["sample_id"]
        managed = False
        verbose_name_plural = "icons"

class Storage(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=200, default='')
    address_1 = models.CharField(max_length=200, default='')
    address_2 = models.CharField(max_length=200, default='')
    region = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=200, default="Turkey")
    created_by = models.CharField(max_length=200)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT)
    orderby = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.store_name

    class Meta():
        managed=False
        db_table = 'kap\".\"store'
        ordering = ["orderby"]
        verbose_name_plural = "stores"

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    store_id = models.ForeignKey(Storage, db_column='store_id', on_delete = models.PROTECT)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', on_delete = models.PROTECT, null=True, blank=True)
    location_type = models.CharField(max_length=100, blank=True, null=True)
    location_name = models.CharField(max_length=100, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.location_name)

    class Meta():
        managed=False
        db_table = 'kap\".\"location'
        ordering = ["orderby"]
        verbose_name_plural = "locations"

class Sample(models.Model): #like a user

    sample_id = models.AutoField(primary_key=True)
    # containers = models.ManyToManyField(Container, through='JoinSampleContainer', through_fields=('sample_id', 'container_id'), related_name='sample')
    area_easting = models.IntegerField(choices = EASTING_CHOICES)
    area_northing = models.IntegerField(choices = NORTHING_CHOICES)
    context_number = models.IntegerField()
    sample_number = models.IntegerField()
    sample_type = models.CharField(max_length=200, default='', blank=True, null=True, choices = MATERIALS)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    recovery_method = models.CharField(max_length=200, default='', blank=True, null=True, choices = RECOVERY_METHODS)
    taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT, related_name='depotsample_taken_by')
    # taken_by = models.IntegerField()
    # taken_by = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='taken_by', on_delete = models.PROTECT)
    # taken_by = models.ForeignKey(public.auth_user, db_column='taken_by', on_delete = models.PROTECT)
    comments = models.CharField(max_length=1000, default='', blank=True, null=True)

    def __str__(self):
        # return self.taken_by.first_name
        return str(self.sample_number)
        # return str(self.firstname)+ '-' +str(self.lastname)
        # return u'%s %s' % (self.first_name, self.last_name)


    class Meta:
        db_table = 'kap\".\"sample'
        #ordering = ["sample_id"]
        managed = True
        #verbose_name_plural = "samples"

class Container(models.Model): #like a friend
    container_id = models.AutoField(primary_key=True)
    # samples = models.IntegerField()
    # samples = models.ManyToManyField(Sample, through='JoinSampleContainer', through_fields=('container_id', 'sample_id'), related_name='containers')
    # samples = models.ManyToManyField(Sample, related_name='containers')
    container_name = models.CharField(max_length=50, blank=True, null=True)
    container_type = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.ForeignKey(Location, db_column='location_id', on_delete = models.PROTECT)
    icon_desc = models.ForeignKey(Icon, db_column='icon_desc', null=True, blank=True, default='Box',on_delete = models.PROTECT)
    samples = models.ManyToManyField('Sample')

    def __str__(self):
        return self.container_name

    class Meta():
        managed=True
        db_table = 'kap\".\"container'
        # ordering = ["container_type"]
        # verbose_name_plural = "containers"
        #unique_together = [('area_easting', 'area_northing', 'context_number', 'sample_number'),]

class JoinSampleContainer(models.Model):
    id = models.AutoField(primary_key=True)
    container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
    sample_id = models.ForeignKey(Sample, db_column='sample_id', on_delete = models.PROTECT)

    def __int__(self):
        return self.id

    class Meta():
        managed=False
        db_table = 'kap\".\"joinsamplecontainer'
        ordering = ["container_id","id"]
        #verbose_name_plural = "Sample Container Join"
        #unique_together = [('area_easting', 'area_northing', 'context_number', 'sample_number'),]





# class Person(models.Model):
#     name = models.CharField(max_length=128)
#
# class Group(models.Model):
#     name = models.CharField(max_length=128)
#     members = models.ManyToManyField(Person, through='Membership')
#
# class Membership(models.Model):
#     person = models.ForeignKey(Person, on_delete = models.PROTECT)
#     group = models.ForeignKey(Group,  on_delete = models.PROTECT)
#     date_joined = models.DateField()
#     invite_reason = models.CharField(max_length=64)


# class Samples(models.Model):
#
#     #container_id = models.ForeignKey(Container, db_column='container_id', on_delete = models.PROTECT)
#     sample_id = models.IntegerField(blank=True, null=True)
#     #sample_id = models.AutoField(primary_key=True)
#
#     #container_id = models.IntegerField()
#
#     area_easting = models.IntegerField()
#     area_northing = models.IntegerField()
#     context_number = models.IntegerField()
#     sample_number = models.AutoField(primary_key=True)
#
#     material = models.CharField(max_length=25)
#     specific_material = models.CharField(max_length=50, blank=True, null=True)
#     exterior_color_hue = models.CharField(max_length=6, blank=True, null=True)
#     exterior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     exterior_color_chroma = models.IntegerField(blank=True, null=True)
#     interior_color_hue = models.CharField(max_length=6, blank=True, null=True)
#     interior_color_lightness_value = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
#     interior_color_chroma = models.IntegerField(blank=True, null=True)
#     weight_kilograms = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
#     sample_description = models.TextField(blank=True, null=True)
#     category = models.CharField(max_length=25, blank=True, null=True)
#     subcategory = models.CharField(max_length=50, blank=True, null=True)
#     count = models.IntegerField(blank=True, null=True)
#     current_location = models.CharField(max_length=50)
#     recovery_type = models.CharField(max_length=25)
#     problems = models.CharField(max_length=300, blank=True, null=True)
#     image_files = models.CharField(max_length=50, blank=True, null=True)
#     number_3d_files = models.CharField(db_column='3d_files', max_length=50, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     chronology = models.CharField(max_length=100, blank=True, null=True)
#     analysis_request = models.CharField(max_length=50, blank=True, null=True)
#     detailed_sample_description = models.TextField(blank=True, null=True)
#     bureaucratic_status = models.CharField(max_length=25, blank=True, null=True)
#     subjective_significance = models.NullBooleanField()
#     museum_inventory_number = models.IntegerField(blank=True, null=True)
#     bureaucratic_status_identifier = models.CharField(max_length=100, blank=True, null=True)

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

    # def __str__(self):
    #     return str(self.sample_number)
    #
    # class Meta:
    #     db_table = 'kap\".\"samples'
    #     #ordering = ["sample_id"]
    #     managed = False
    #     #verbose_name_plural = "samples"
    #     #unique_together = (('area_easting', 'area_northing', 'context_number', 'sample_number'),)




# m2m test
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete = models.PROTECT)
    # container_id = models.ForeignKey(Container, null=True, on_delete = models.PROTECT)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

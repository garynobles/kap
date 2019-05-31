from django.db import models
from django.contrib.auth.models import User
import datetime
# from safedelete.models import SafeDeleteModel
# from safedelete.models import HARD_DELETE_NOCASCADE

TRUE_FALSE_CHOICES = (
    ("",""),
    (True, 'Yes'),
    (False, 'No')
)
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
NORTHING_CHOICES = (
    ("",""),
    (523, 523),
    (526, 526),
    (551,551),
    (536,536),
    (545,545),
    (555,555),
    (541,541),
    (531,531),
    (987,987),
)

COMPUTER_CHOICES = (
    ("",""),
    ("Artaphernes","Artaphernes"),
    ("Cyrus","Cyrus"),
    ("Harpagus","Harpagus"),
    ("Pissuthnes", "Pissuthnes"),
    ("Struthas", "Struthas"),
    ("Tissaphernes","Tissaphernes"),


)




#boolfield = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Some Label", initial='', widget=forms.Select(), required=True)
class Photobatch(models.Model):
    # _safedelete_policy = HARD_DELETE_NOCASCADE
    #_safedelete_visibility = DELETED_VISIBLE_BY_PK

    pb_id = models.AutoField(primary_key=True)
    #id = models.IntegerField(blank=True, null=True)
    photobatch_id = models.CharField(max_length=200, default='', blank=True, null=True)
    prefix = models.CharField(max_length=200, default='', blank=True, null=True)

    area_easting = models.IntegerField(null=False, choices = EASTING_CHOICES)
    area_northing= models.IntegerField(null=False, choices = NORTHING_CHOICES)
    context_number = models.IntegerField(null=False)
    #
    number_of_photos = models.IntegerField(blank=True, null=True)
    number_targets = models.IntegerField(blank=True, null=True)
    processed_on = models.CharField(max_length=200, default='', blank=True, null=True, choices = COMPUTER_CHOICES)
    processed_by = models.CharField(max_length=200, default='', blank=True, null=True)
    camera_model = models.CharField(max_length=200, default='samsung', blank=True, null=True)
    imported_photoscan = models.NullBooleanField()
    #
    aligned = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    align_accuracy = models.CharField(max_length=200, default="medium")
    align_pair_selection = models.CharField(max_length=200, default="disabled")
    align_keypoint_limit = models.IntegerField(default= 40000)
    align_tiepoint_limit = models.IntegerField(default= 4000)
    #
    detected_targets = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    target_type = models.CharField(max_length=200, default="circular 12 bit")
    target_tolerance = models.IntegerField(default= 50)
    target_origional_error = models.IntegerField(blank=True, null=True)
    target_optimised_error = models.IntegerField(blank=True, null=True)
    #
    dense_pointcloud = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    #
    mesh = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    mesh_type= models.CharField(max_length=200, default="arbitrary")
    mesh_face_count= models.CharField(max_length=200, default="medium")
    mesh_interpolation = models.CharField(max_length=200, default="disabled")
    #
    texture = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    texture_defaults = models.IntegerField(blank=True, null=True, default=8500)
    dem = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    dem_coordinate_system = models.IntegerField(default= 32635)
    dem_source_data= models.CharField(max_length=200, default="dense cloud")
    dem_interpolation= models.CharField(max_length=200, default="disabled")
    #
    orthomosaic= models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    orthomosaic_type = models.CharField(max_length=200, default="geographic")
    orthomosaic_pixel_size = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True, default = 0.005)
    #
    export_points= models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    export_points_filename = models.CharField(max_length=100, default="", blank=True, null=True)
    export_points_offsets = models.CharField(max_length=200, default="X=580000 Y=4275000 Z=0")
    #
    export_report_pdf= models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    export_orthophoto= models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    export_dem = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    export_dem_pixel_size = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=6, default=0.005 )
    export_dem_geodatabase = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    folder_processed = models.NullBooleanField(choices = TRUE_FALSE_CHOICES)
    processing_notes = models.TextField(blank=True, null=True)
    #image = models.ImageField(upload_to='images/notes/',blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, default="user_not_defined")
    #
    def __str__(self):
        return self.photobatch_id

    class Meta():
        managed=False
        db_table = 'excavation\".\"photobatch_processing'
        ordering = ["-folder_processed", "-created_timestamp"]

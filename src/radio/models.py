from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.files import File
from PIL import Image, ImageOps
from io import BytesIO
from core import validators

def Station_Cover_Images(instance, filename):
    return '/'.join(['Media_Files', 'Station_Cover_Images', str(instance.station_name) + "_" + str(filename)])

class RadioStationModel(models.Model):
    
    class Meta:
        ordering = ['id']

    station_name = models.CharField(null=False, blank=True, unique=True, max_length=256)
    station_frequency = models.FloatField(null=False, blank=False, unique=True)
    station_url = models.CharField(null=False , blank=True, max_length=1023)
    station_cover = models.ImageField(upload_to=Station_Cover_Images, validators=[validators.validate_image_extension], null=False, blank=True)
    station_description = models.TextField(blank=True, null=True, max_length=1023)
    encoder_FUI =  models.CharField(null=False, blank=True, max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_passstation_frequency_for_es(self):
        string_frequency = str(self.station_frequency)
        return string_frequency

    def __str__(self):
        return f"{self.pk}: {self.station_name}"

    def save(self, *args, **kwargs):
        image = Image.open(self.station_cover)
        image = image.convert('RGB')
        image = ImageOps.exif_transpose(image)
        image_io = BytesIO()
        image.save(image_io, "JPEG", optimize=True, quality=50)
        compressed_image = File(image_io, name=str(self.station_cover))
        self.station_cover = compressed_image
        super(RadioStationModel, self).save(*args, **kwargs)

class FavouritesModel(models.Model):

    class Meta:
        ordering = ['id']
    
    station_id = models.ForeignKey(RadioStationModel, default=1, on_delete=models.CASCADE, null=False, blank=False)
    user_FUI =  models.CharField(max_length=1023, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.user_FUI}"
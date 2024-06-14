from django.db import models
from django.contrib.gis.db import models as gismodels
import django.contrib.gis.geos as geos

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    point = gismodels.PointField(srid=4326, null=True, blank=True,default=geos.Point(0.0,0.0,srid=4326),geography=True)
from django.db import models
from django.conf import settings

# Create your models here.
class Pirate(models.Model):
    name = models.CharField(max_length=100)
    life = models.CharField(max_length=20)
    years_active = models.CharField(max_length=20)
    country_of_origin = models.CharField(max_length=20)
    comments = models.CharField(max_length=200, blank=False, default='')
    def __str__(self):
      return self.name

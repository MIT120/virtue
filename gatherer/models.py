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

ENUMCHOICES = (
    ('y', 'On'),
    ('n', 'Off'),
)
class Appliance(models.Model):
    flat_id = models.Foreign_key(Flat, on_delete=models.CASCADE, primary_key=True, max_length=45)
    room_id = models.Foreign_key(Room, on_delete=models.CASCADE, primary_key=True, max_length=45)
    appliance_id = models.CharField(primary_key=True, max_length=45)
    appliance_type_id = models.Foreign_key(List_Of_All_Appliance_in_building, on_delete=models.CASCADE, primary_key=True)
    appliance_status = models.CharField(max_length=1, choices=ENUMCHOICES)
    last_appliance_energy_consumed = models.FloatField(null=True)
    last_reading_time = models.DateField()
class List_Of_All_Appliance_in_building(models.Model):
    appliance_type_id = models.AutoField(primary_key=True)
    appliance_name = models.CharField(max_length=45)
    appliance_power = models.IntegerField()
class Appliance_Readings(models.Model):
    reading_time = models.DateField(primary_key=True)
    flat_id = models.Foreign_key(Flat, on_delete=models.CASCADE, max_length=45)
    room_id = models.Foreign_key(Room, on_delete=models.CASCADE, max_length=45)
    appliance_id = models.Foreign_key(Appliance, on_delete=models.CASCADE, max_length=45)
    appliance_type_id = models.Foreign_key(List_Of_All_Appliance_in_building, on_delete=models.CASCADE)
    appliance_energy_consumed = models.FloatField(null=True)



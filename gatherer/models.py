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

class Building(models.Model):
  building_id = models.IntegerField(primary_key=True)
  city = models.CharField(max_length=50)
  street = models.CharField(max_length=45)
  postcode = models.CharField(max_length=45)
  country = models.CharField(max_length=45)
  nr_Of_Floors = models.IntegerField()
  building_name = models.CharField(max_length=45)

class Flat(models.Model):
    flat_id = models.CharField(max_length=45, primary_key=True)
    floor_nr = models.IntegerField()
    time_created = models.DateField()
    time_updated = models.DateField()
    type = models.CharField(max_length=45)
    nr_of_people = models.IntegerField()
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    flat_rating = models.FloatField(null=True)

class Room(models.Model):
  flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE, primary_key=True)
  room_id = models.CharField(max_length=45, primary_key=True)
  room_name = models.CharField(max_length=45)
  last_humidity = models.FloatField(null=True)
  last_temperature = models.FloatField(null=True)
  last_amount_CO2 = models.FloatField(null=True)
  last_reading_time = models.DateField()
  nr_of_appliances = models.IntegerField()

class Room_Readings(models.Model):
  reading_time = models.DateField(primary_key=True)
  flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE)
  room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

class Weather(models.Model):
  weather_id = models.AutoField(primary_key=True)
  building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
  reading_time = models.DateField()
  temperature = models.FloatField(null=True)
  humidity = models.FloatField(null=True)
  windspeed = models.IntegerField()
  wind_direction = models.IntegerField()
  solar_rediation = models.FloatField(null=True)
  amount_of_CO2 = models.FloatField(null=True)

class List_Of_All_Appliance_in_building(models.Model):
    appliance_type_id = models.AutoField(primary_key=True)
    appliance_name = models.CharField(max_length=45)
    appliance_power = models.IntegerField()

class Appliance(models.Model):
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE, primary_key=True, max_length=45)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, primary_key=True, max_length=45)
    appliance_id = models.CharField(primary_key=True, max_length=45)
    appliance_type_id = models.ForeignKey(List_Of_All_Appliance_in_building, on_delete=models.CASCADE, primary_key=True)
    appliance_status = models.CharField(max_length=1, choices=ENUMCHOICES)
    last_appliance_energy_consumed = models.FloatField(null=True)
    last_reading_time = models.DateField()


class Appliance_Readings(models.Model):
    reading_time = models.DateField(primary_key=True)
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE, max_length=45)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, max_length=45)
    appliance_id = models.ForeignKey(Appliance, on_delete=models.CASCADE, max_length=45)
    appliance_type_id = models.ForeignKey(List_Of_All_Appliance_in_building, on_delete=models.CASCADE)
    appliance_energy_consumed = models.FloatField(null=True)

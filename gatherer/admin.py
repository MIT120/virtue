from django.contrib import admin
from . import models

class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_function')
    model = models.Sensor

admin.site.register(models.Sensor, SensorAdmin)
admin.site.register(models.Building)
admin.site.register(models.Room)
admin.site.register(models.Flat)
admin.site.register(models.Room_Reading)
admin.site.register(models.Sensor_Reading)
admin.site.register(models.Appliance)
admin.site.register(models.Appliance_Reading)
# Register your models here.

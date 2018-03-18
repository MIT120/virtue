from django.contrib import admin
from . models import Pirate, Sensor, Building, Weather

class SensorAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'sensor_function')
    model = Sensor



admin.site.register(Pirate)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Building)
admin.site.register(Weather)
# Register your models here.

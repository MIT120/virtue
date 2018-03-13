from rest_framework import serializers
from .models import Pirate

class PirateSerializer(serializers.ModelSerializer):

   class Meta:
     model = Pirate
     fields = '__all__'

class SensorSelrializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sensor_id', 'sensor_name', 'sensor_function']



class Sensor_ReadingSelrializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Reading
        fields = ['sensor_id', 'unit_id', 'which_appliance']


class UnitsSelrializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['unit_id', 'unit_for', 'unit']


class ApplianceSelrializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance
        fields = ['flat_id', 'room_id', 'appliance_id', 'appliance_type_id', 'appliance_status', 'last_appliance_energy_consumed', 'last_reading_time']


class List_Of_All_Appliance_in_buildingSelrializer(serializers.ModelSerializer):
    class Meta:
        model = List_Of_All_Appliance_in_building
        fields = ['appliance_type_id', 'appliance_name', 'appliance_power']


class Appliance_ReadingSelrializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance_Reading
        fields = ['flat_id', 'room_id', 'appliance_id','appliance_type_id', 'last_appliance_energy_consumed']

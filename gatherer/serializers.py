from rest_framework import serializers
from .models import Sensor, Appliance, Appliance_Reading , Building, Flat, List_Of_All_Appliance_in_building, Room, Room_Reading, Unit, Weather, Sensor_Reading

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class Sensor_ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Reading
        fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

class ApplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance
        fields = "__all__"

class List_Of_All_Appliance_in_buildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = List_Of_All_Appliance_in_building
        fields = "__all__"

class Appliance_ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliance_Reading
        fields = "__all__"

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"

class Room_ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Reading
        fields = "__all__"

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

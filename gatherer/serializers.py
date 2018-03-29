from rest_framework import serializers
from .models import Sensor, Appliance, Appliance_Reading, Person_Sleep, Personal_details, Building, Flat, List_Of_All_Appliance_in_building, Room, Room_Reading, Unit, Weather, Sensor_Reading

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class Sensor_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor_Reading
        fields = "__all__"


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"

class ApplianceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance
        fields = "__all__"

class List_Of_All_Appliance_in_buildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List_Of_All_Appliance_in_building
        fields = "__all__"

class Appliance_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appliance_Reading
        fields = "__all__"

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class FlatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flat
        fields = "__all__"

class Room_ReadingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room_Reading
        fields = "__all__"

class WeatherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'

class Person_SleepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person_Sleep
        fields = '__all__'

class Personal_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personal_details
        fields = '__all__'

class BuildingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

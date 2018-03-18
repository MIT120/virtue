from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorSerializer, BuildingSerializer, WeatherSerializer, FlatSerializer,Room_ReadingSerializer, RoomSerializer, Sensor_ReadingSerializer, UnitSerializer, ApplianceSerializer , List_Of_All_Appliance_in_buildingSerializer , Appliance_ReadingSerializer
from .models import Sensor, Building, Weather, Flat, Room_Reading, Room, Sensor_Reading, Unit, Appliance, List_Of_All_Appliance_in_building, Appliance_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
import json
#views here.

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

class FlatViewSet(viewsets.ModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

class List_Of_All_Appliance_in_buildingViewSet(viewsets.ModelViewSet):
    queryset = List_Of_All_Appliance_in_building.objects.all()
    serializer_class = List_Of_All_Appliance_in_buildingSerializer

class Appliance_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Appliance_Reading.objects.all()
    serializer_class = Appliance_ReadingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class Room_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Room_Reading.objects.all()
    serializer_class = Room_ReadingSerializer

class Sensor_ReadingViewSet(viewsets.ModelViewSet):
    queryset = Sensor_Reading.objects.all()
    serializer_class = Sensor_ReadingSerializer

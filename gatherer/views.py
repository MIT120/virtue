from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import SensorSerializer, BuildingSerializer, WeatherSerializer, FlatSerializer, UnitSerializer, ApplianceSerializer , List_Of_All_Appliance_in_buildingSerializer , Appliance_ReadingSerializer
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

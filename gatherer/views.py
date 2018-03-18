from django.shortcuts import render, HttpResponse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import PirateSerializer, SensorSerializer, BuildingSerializer, WeatherSerializer, FlatSerializer, UnitSerializer, ApplianceSerializer , List_Of_All_Appliance_in_buildingSerializer , Appliance_ReadingSerializer
from .models import Pirate, Sensor, Building, Weather, Flat, Room_Reading, Room, Sensor_Reading, Unit, Appliance, List_Of_All_Appliance_in_building, Appliance_Reading
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from .serializers import PirateSerializer
import json
# Create your views here.
class APIRootView(APIView):

#  def json_list(self, request):
 #   url = 'https://i886625.venus.fhict.nl/pirates.json'
#    r = requests.get(url)
#    json_data = r.json()
#    json_pretty = json.dumps(json_data, sort_keys=True, indent=4)

#    context = {
#        "json_pretty": json_pretty,
#        }
#    return render(request, "templates/json.html", context)
    def get(self, request):
        pirates = Pirate.objects.all()
        serializer = PirateSerializer(pirates, many=True)
        return Response(serializer.data)


    def post(self):
      pass


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer



class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class WeatherViewSet(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

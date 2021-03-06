"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views


router = routers.DefaultRouter()
router.register('building', views.BuildingViewSet)
router.register('sensor', views.SensorViewSet)
router.register('weather', views.WeatherViewSet)
router.register('appliance_reading', views.Appliance_ReadingViewSet)
router.register('appliance', views.ApplianceViewSet)
router.register('appliances_in_building', views.List_Of_All_Appliance_in_buildingViewSet)
router.register('flat', views.FlatViewSet)
router.register('room', views.RoomViewSet)
router.register('room_reading', views.Room_ReadingViewSet)
router.register('sensor_reading', views.Sensor_ReadingViewSet)
router.register('personal_details', views.Personal_detailsViewSet)
router.register('person_sleep', views.Person_SleepViewSet)
router.register('unit', views.UnitViewSet)




urlpatterns = [
  path('', include(router.urls))
]

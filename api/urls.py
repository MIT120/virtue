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
from django.contrib import admin
from django.conf.urls import  url, include
from django.contrib.auth.models import User
from django.urls import path, re_path
from rest_framework import routers, serializers, viewsets
from weather.views import WeatherViewSet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()
router.register(r'', UserViewSet)

#router.register(r'accounts', AccountViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appliance/',include('appliance.urls')),
    path('appliance_in_building/',include('appliance.urls')),
    path('appliance_reading/',include('appliance_reading.urls')),
    path('building/',include('building.urls')),
    path('flat/',include('flat.urls')),
    path('person_sleep/',include('person_sleep.urls')),
    path('personal_details/',include('personal_details.urls')),
    path('room/',include('room.urls')),
    path('room_reading/',include('room_reading.urls')),
    path('sensor/',include('sensor.urls')),
    path('sensor_reading/',include('sensor_reading.urls')),
    path('unit/',include('unit.urls')),
    path('weather/',include('weather.urls')),
    path('users/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

 ]

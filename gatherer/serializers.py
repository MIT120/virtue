from rest_framework import serializers
from .models import Pirate

class PirateSerializer(serializers.ModelSerializer):

   class Meta:
     model = Pirate
     fields = '__all__'
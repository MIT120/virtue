from rest_framework import serializers
from .model import Pirate

class PirateSerializer(serializers.ModelSerializer):

   class Meta:
     model = Pirate
     fields = '__all__'
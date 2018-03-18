from rest_framework import serializers
from .models import Sensor, Appliance, Appliance_Reading, Person_Sleep, Personal_details, Building, Flat, List_Of_All_Appliance_in_building, Room, Room_Reading, Unit, Weather, Sensor_Reading

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = "__all__"

class Sensor_ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Reading
        fields = "__all__"

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        # Perform deletions.
        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret

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

class Person_SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person_Sleep
        fields = '__all__'

class Personal_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_details
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

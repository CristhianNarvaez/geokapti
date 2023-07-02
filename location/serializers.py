from rest_framework import serializers
from location import models as location_model

class Location(serializers.ModelSerializer):
    class Meta:
        model = location_model.Location
        fields = ["id", "name", "latitude", "longitude"]

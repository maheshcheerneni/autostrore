from rest_framework import serializers
from .models import Bike,Bikemodels

class Bike_serliazer(serializers.ModelSerializer):
    class Meta:
        model =Bikemodels
        fields = '__all__'
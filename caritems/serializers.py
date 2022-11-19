from rest_framework import serializers
from .models import Car_details,Company




class Car_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Car_details
        fields='__all__'
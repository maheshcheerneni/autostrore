from django.shortcuts import render
from .serializers import Car_Serializer
from .models import Car_details,Company
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# Create your views here.


class Carlist_view(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request):
        car_serializer = Car_Serializer(data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({"status": "success", "data": car_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": car_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        query = Car_details.objects.all()
        serializer = Car_Serializer(query, many=True)
        return Response(serializer.data)
class Detail_view(APIView):
    def get(self,request,sino):
        query = Car_details.objects.filter(id=sino)
        serializer = Car_Serializer(query,many=True)
        return Response(serializer.data)

    def put(self,request,sino):
        query = Car_details.objects.get(id=sino)
        update = Car_Serializer(query,data=request.data)
        if update.is_valid():
            update.save()
            return Response(update.data)
        return Response(update.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,sino):
        query = Car_details.objects.filter(id=sino)
        query.delete()
        return Response(query,status=status.HTTP_204_NO_CONTENT)

    
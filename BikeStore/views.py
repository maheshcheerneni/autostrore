from django.shortcuts import render
from .models import Bikemodels,Bike
from .serializers import Bike_serliazer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
# Create your views here.
# LIST THE DATA
class bike_list(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = Bikemodels.objects.all()
    serializer_class = Bike_serliazer
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
class bike_detailed(mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Bikemodels.objects.all()
    serializer_class = Bike_serliazer
# READ THE DATA
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
# ON UPDATE DATA
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
# ON CREATE DATA
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    
# ON DELETE DATA
    def delete(self,request,*args, **kwargs):
        return self.delete(request,*args, **kwargs)
    

from email.policy import default
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.   

# class TourIndiaCRED():  
  
    # def get(self,request):
    #     st = State.objects.all()
    #     serializer = stateSerializers(st,many=True)      
    #     return Response({'States':serializer.data})

    # def post(self,request):
    #     serializer = stateSerializers(data=request.data)
    #     if not serializer.is_valid(raise_exception=True):
    #         return Response({'Mesages':404})
    #     serializer.save()
    #     return Response({'Updated':serializer.data})
  
    # def put(self,request):
    #     return Response({'Status':200})

    # def delete(self,request):
    #     return Response({'Status':200})

class TourgenericGP(generics.ListAPIView,generics.CreateAPIView):     
    queryset = State.objects.all()
    serializer_class = stateSerializers

class TourgenericPD(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = State.objects.all()
    serializer_class = stateSerializers
    lookup_field = 'Id'

class CategoryGenerics(generics.ListAPIView,generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializers
    
class CategoryGenericsPD(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializers
    lookup_field = 'Id'

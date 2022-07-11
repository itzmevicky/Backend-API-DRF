from rest_framework import serializers
from .models import *

class categorySerializers(serializers.ModelSerializer):        
    class Meta :
        model = Category
        fields = '__all__'

class stateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['Id','Name','Descriptions']

# shaheen

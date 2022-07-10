from django.db import models
from .helper import baseModel
# Create your models here.

class  Category(baseModel):
    categoryStatus = models.BooleanField()   

class State(baseModel):
    pass

class Zone(baseModel):
    pass

class TypeOfPackage(baseModel):
    pass

class Pacakges(baseModel):
    PackageId = models.AutoField(primary_key=True)
    PackgesDurations = models.DurationField(null=True,blank=True)
    PackagesInclusion = models.TextField(null=True,blank=True)

class IternaryItems(baseModel):
    Title = models.CharField(max_length=100)
    Day = models.DateField()

    

    

    


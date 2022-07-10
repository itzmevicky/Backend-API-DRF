
from django.db import models
from django.contrib import admin

class baseModel(models.Model):
    Id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length= 100)
    Descriptions = models.TextField(blank=True,null=True)
    Image = models.ImageField()    
    def __str__(self) :
        return self.Name

class listOfFields(admin.ModelAdmin):    
        list_display = ['Id','Name','Descriptions','Image']
        
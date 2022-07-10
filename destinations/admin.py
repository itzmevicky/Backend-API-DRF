
from django.contrib import admin
from .models import *
from .helper import listOfFields
# Register your models here.

# class DemAdm(admin.ModelAdmin):
#     list_display = ['Name','age']

admin.site.register(Category,listOfFields)
admin.site.register(State,listOfFields)
admin.site.register(Zone,listOfFields)
admin.site.register(TypeOfPackage,listOfFields)
admin.site.register(Pacakges,listOfFields)
admin.site.register(IternaryItems,listOfFields)
# admin.site.register(demoSerializers,DemAdm)


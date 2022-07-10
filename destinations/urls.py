from django.urls import path
from .views import *

urlpatterns = [
   # path('', TourIndiaCRED.as_view())
   path('',TourgenericGP.as_view()),
   path('PD/<Id>',TourgenericPD.as_view()),
   path('Cat/',CategoryGenerics.as_view()),
   path('Cat/<Id>/',CategoryGenericsPD.as_view())
]
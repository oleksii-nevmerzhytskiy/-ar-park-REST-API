from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('driver/', DriverView.as_view()),
    path('driver/<int:pk>/', DriverById.as_view()),
    path('vehicle/', VehicleView.as_view()),
    path('vehicle/<int:pk>/', VehicleViewById.as_view()),
    path('set_driver/<int:pk>/', VehicleSetDriver.as_view()),
]

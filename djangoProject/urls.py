from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/', include('Car_park.urls')),
    path('vehicles/', include('Car_park.urls')),
]

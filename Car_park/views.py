from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from datetime import datetime


class DriverView(APIView):

    def get(self, request):
        if self.request.GET.get('created_at__gte'):
            date = datetime.strptime(self.request.GET.get('created_at__gte'), '%d-%m-%Y')
            drivers = Driver.objects.filter(created_at__gte=date)
        elif self.request.GET.get('created_at__lte'):
            date = datetime.strptime(self.request.GET.get('created_at__lte'), '%d-%m-%Y')
            drivers = Driver.objects.filter(created_at__lte=date)
        else:
            drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response({"driver": serializer.data})

    def post(self, request):
        driver = request.data.get('driver')
        serializer = DriverSerializer(data=driver, partial=True)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({"success": "Driver '{}' created successfully".format(driver_saved.id)})


class DriverById(APIView):
    def get(self, request, pk=1):
        drivers = Driver.objects.filter(id=pk)
        serializer = DriverSerializer(drivers, many=True)
        return Response({"driver": serializer.data})

    def put(self, request, pk=1):
        saved_driver = get_object_or_404(Driver.objects.all(), id=pk)
        data = request.data.get('driver')
        driver_serializer = DriverSerializer(instance=saved_driver, data=data, partial=True)
        serializer = driver_serializer

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "success": "Driver '{}' updated successfully".format(pk)})

    def delete(self, request, pk=1):
        driver = get_object_or_404(Driver.objects.all(), id=pk)
        driver.delete()
        return Response({
            "message": "Driver with id `{}` has been deleted.".format(pk)
        }, status=204)


class VehicleView(APIView):
    def get(self, request):
        if self.request.GET.get('with_drivers') == "yes":
            vehicles = Vehicle.objects.filter(driver__isnull=False)
        elif self.request.GET.get('with_drivers') == "no":
            vehicles = Vehicle.objects.filter(driver__isnull=True)
        else:
            vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"vehicle": serializer.data})

    def post(self, request):
        vehicle = request.data.get('vehicle')
        serializer = VehicleSerializer(data=vehicle, partial=True)
        if serializer.is_valid(raise_exception=True):
            driver_saved = serializer.save()
        return Response({"success": "Vehicle '{}' created successfully".format(driver_saved.id)})


class VehicleViewById(APIView):
    def get(self, request, pk=1):
        vehicles = Vehicle.objects.filter(id=pk)
        serializer = VehicleSerializer(vehicles, many=True)
        return Response({"vehicle": serializer.data})

    def put(self, request, pk=1):
        saved_vehicle = get_object_or_404(Vehicle.objects.filter(id=pk))
        data = request.data.get('vehicle')
        vehicle_serializer = VehicleSerializer(instance=saved_vehicle, data=data, partial=True)
        serializer = vehicle_serializer

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({
                "success": "Vehicle '{}' updated successfully".format(pk)
            })

    def delete(self, request, pk=1):
        vehicle = get_object_or_404(Vehicle.objects.all(), id=pk)
        vehicle.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)


class VehicleSetDriver(APIView):
    def get(self, request, pk=1):
        drivers = Vehicle.objects.filter(id=pk)
        serializer = VehicleSerializer(drivers, many=True)
        return Response({"vehicle": serializer.data})

    def post(self, request, pk=1):
        saved_vehicle = get_object_or_404(Vehicle.objects.all(), id=pk)
        data = request.data.get('vehicle')
        vehicle_serializer = VehicleSerializer(instance=saved_vehicle, data=data, partial=True)
        serializer = vehicle_serializer

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "success": "Vehicle '{}' updated successfully".format(pk)})

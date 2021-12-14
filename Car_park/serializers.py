# from rest_framework import serializers
# from .models import Driver, Vehicle
#
#
# class DriverSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Driver.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         return Driver.objects.update(**validated_data)
#
#
# class VehicleSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     driver_id = serializers.IntegerField(allow_null=True)
#     make = serializers.CharField(max_length=50)
#     model = serializers.CharField(max_length=50)
#     plate_number = serializers.CharField(max_length=50)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#
#     def create(self, validated_data):
#         return Vehicle.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         return Vehicle.objects.update(**validated_data)






from rest_framework import serializers
from .models import Driver, Vehicle


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ("id", "first_name", "last_name", "created_at", "updated_at")

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("id", "driver", "make", "model", "plate_number", "created_at", "updated_at")
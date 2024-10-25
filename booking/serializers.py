from rest_framework import serializers
from .models import Booking

class PriceCalculationSerializer(serializers.Serializer):
    pickup_time = serializers.DateTimeField()
    return_time = serializers.DateTimeField()
    car_id = serializers.IntegerField()


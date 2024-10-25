
from rest_framework import serializers
from .models import Car
from django.shortcuts import get_object_or_404


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'




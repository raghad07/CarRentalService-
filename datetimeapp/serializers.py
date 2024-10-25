# myapp/serializers.py

from rest_framework import serializers
from .models import MyData

class MyDataSerializer(serializers.ModelSerializer):
    number_of_days = serializers.ReadOnlyField() 
    #total_price = serializers.SerializerMethodField() 



    class Meta:
        model = MyData
        fields = '__all__'

     


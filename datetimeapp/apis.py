# myapp/api.py

from rest_framework import generics
from .models import MyData
from .serializers import MyDataSerializer
from rest_framework import filters
from django.shortcuts import get_object_or_404






class MyDataListCreate(generics.ListCreateAPIView):
    queryset = MyData.objects.all()
    serializer_class = MyDataSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['start_data', 'return_data']





class MyDataRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyData.objects.all()
    serializer_class = MyDataSerializer



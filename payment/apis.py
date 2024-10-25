from rest_framework import generics
from .models import PersonalDetails
from .serializers import PersonalDetailsSerializer

class PersonalDetailsListCreateAPIView(generics.ListCreateAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

class PersonalDetailsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer

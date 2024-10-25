from rest_framework import generics
from .models import Booking

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from brands.models import Car
from payment.models import PersonalDetails
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from brands.models import Car
from payment.models import PersonalDetails
from datetime import datetime




from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import PriceCalculationSerializer
from brands.models import Car
from datetime import datetime

class CalculateTotalPriceAPIView(generics.GenericAPIView):
    serializer_class = PriceCalculationSerializer  

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        pickup_time = serializer.validated_data['pickup_time']
        return_time = serializer.validated_data['return_time']
        car_id = serializer.validated_data['car_id']

        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

        rental_days = (return_time - pickup_time).days
        if rental_days <= 0:
            return Response({"error": "Return time must be after pickup time."}, status=status.HTTP_400_BAD_REQUEST)

        total_price = rental_days * car.price

        return Response({"total_price": total_price}, status=status.HTTP_200_OK)

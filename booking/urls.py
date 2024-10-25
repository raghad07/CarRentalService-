from django.urls import path
from .apis import CalculateTotalPriceAPIView

from django.urls import path
from .apis import CalculateTotalPriceAPIView

urlpatterns = [
    path('calculate-price/', CalculateTotalPriceAPIView.as_view(), name='calculate-price'),
]


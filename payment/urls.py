from django.urls import path
from .apis import PersonalDetailsListCreateAPIView, PersonalDetailsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('personal-details/', PersonalDetailsListCreateAPIView.as_view(), name='personal-details-list-create'),
    path('personal-details/<int:pk>/', PersonalDetailsRetrieveUpdateDestroyAPIView.as_view(), name='personal-details-retrieve-update-destroy'),
]

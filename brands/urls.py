from django.urls import path
from .apis import CarListCreateAPIView, CarRetrieveUpdateDestroyAPIView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('cars/', CarListCreateAPIView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyAPIView.as_view(), name='car-retrieve-update-destroy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

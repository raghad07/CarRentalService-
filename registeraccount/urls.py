# registeraccount/urls.py

from django.urls import path
from .apis import RegisterView, RegisterView  # Ensure these classes are correctly defined

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', RegisterView.as_view(), name='login'),
]

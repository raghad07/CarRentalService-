
from django.urls import path
from .apis import MyDataListCreate, MyDataRetrieveUpdateDestroy

urlpatterns = [
    path('mydata/', MyDataListCreate.as_view(), name='mydata-list-create'),
    path('mydata/<int:pk>/', MyDataRetrieveUpdateDestroy.as_view(), name='mydata-retrieve-update-destroy'),
]


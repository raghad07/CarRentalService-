from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

class PersonalDetails(models.Model):
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('master', 'MasterCard'),
        ('visa', 'Visa'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    additional_phone_number = models.CharField(max_length=15, blank=True, null=True)
    pickup_address = models.TextField()
    return_address = models.TextField()

    payment_method = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    card_name = models.CharField(max_length=50,null=True)
    card_number = models.CharField(max_length=16,null=True)  
    expiration_date = models.DateField(null=True)
    cvv = models.CharField(max_length=4,null=True) 

 



    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"
    
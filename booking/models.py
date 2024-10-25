from django.db import models
from brands.models import Car
from datetimeapp.models import MyData
from payment.models import PersonalDetails

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    booking_pickup_time = models.ForeignKey(MyData, related_name='pickup_times', on_delete=models.CASCADE)
    booking_return_time = models.ForeignKey(MyData, related_name='return_times', on_delete=models.CASCADE)

    @property
    def total_price(self):
        return (self.booking_return_time.return_time - self.booking_pickup_time.start_time).days * self.car.price

    def __str__(self):
        return f"Booking: {self.customer} - {self.car} from {self.booking_pickup_time.start_time} to {self.booking_return_time.return_time}"

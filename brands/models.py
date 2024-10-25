from django.db import models

from django.db import models

from django.db import models
from django.core.exceptions import ValidationError

class Car(models.Model):
    BRAND_CHOICES = [
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Volvo', 'Volvo'),
        ('Porsche', 'Porsche'),
        ('Jeep', 'Jeep'),
        ('Audi', 'Audi'),
        ('Ferrari', 'Ferrari'),
    ]
    
    CAR_TYPES = [
        ('touring', 'Touring Cars'),
        ('hiking', 'Hiking Cars'),
        ('camping', 'Camping Cars'),
    ]
    
    BRAND_PRICES = {
        'BMW': 500.00,
        'Mercedes': 600.00,
        'Volvo': 550.00,
        'Porsche': 800.00,
        'Jeep': 450.00,
        'Audi': 550.00,
        'Ferrari': 1500.00,
    }
    
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
        ('white', 'White'),
        ('silver', 'Silver'),
        ('yellow', 'Yellow'),
        ('gray', 'Gray'),
    ]
    
    SEAT_CHOICES = [
        (2, '2 seats'),
        (4, '4 seats'),
        (5, '5 seats'),
        (7, '7 seats'),
    ]
    
    DOOR_CHOICES = [
        (2, '2 doors'),
        (4, '4 doors'),
    ]
    
    SUNROOF_CHOICES = [
        (True, 'Yes'),
        (False, 'No'),
    ]
    
    AUTOMATIC_CHOICES = [
        (True, 'Automatic'),
        (False, 'Manual'),
    ]
    
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    number_of_seats = models.PositiveIntegerField(choices=SEAT_CHOICES)
    number_of_doors = models.PositiveIntegerField(choices=DOOR_CHOICES)
    sunroof = models.BooleanField(choices=SUNROOF_CHOICES)
    automatic = models.BooleanField(choices=AUTOMATIC_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES)
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    
    def save(self, *args, **kwargs):
        self.price = self.BRAND_PRICES.get(self.brand, 0.00)
        super().save(*args, **kwargs)




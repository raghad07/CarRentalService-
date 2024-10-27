# account/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Only retain username and email as required fields, password is handled by AbstractUser
    email = models.EmailField(unique=True)  # Ensure email is unique

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

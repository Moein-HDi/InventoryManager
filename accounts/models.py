from django.db import models
from Management.models import City
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
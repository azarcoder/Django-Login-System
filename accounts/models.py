from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CityChoices(models.TextChoices):
    CHENNAI = "CHN", "Chennai"
    TRICHY = "TRI", "Tiruchirappalli"
    COIMBATORE = "CBE", "Coimbatore"


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(
        max_length=3,  # Use appropriate max_length based on the code length
        choices=CityChoices.choices,
        default=CityChoices.CHENNAI,
        null=True,
        blank=True
    )

# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    country = models.CharField(max_length=50)
    founded_year = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(
        CarMake, 
        on_delete=models.CASCADE
    )  # Many-to-One relationship


    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('CONVERTIBLE', 'Convertible'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ]
    type = models.CharField(max_length=11, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )
    horsepower = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transmission = models.CharField(max_length=50)

    def __str__(self):
        return self.name  # Return the name as the string representation

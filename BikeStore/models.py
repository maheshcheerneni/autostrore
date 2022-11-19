from django.db import models

# Create your models here.
class Bike(models.Model):
    company_name=models.CharField(max_length=50)
    sino=models.PositiveIntegerField()

    def __str__(self):
        return self.company_name
class Bikemodels(models.Model):
    sino=models.PositiveIntegerField()
    company_name=models.ForeignKey("Bike", on_delete=models.CASCADE)
    Bike_model=models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    tank_capacity=models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    launch_Date = models.DateField()
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.Bike_model
    
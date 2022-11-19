from django.db import models

# Create your models here.

class Company(models.Model):
    Company_Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Company_Name
class Car_details(models.Model):
    Company_Name=models.ForeignKey("Company",on_delete=models.CASCADE)
    Model_name = models.CharField(max_length=100)
    M_Year = models.DateField(auto_now=False, auto_now_add=False)
    Milage=models.CharField(max_length=50)
    Fuel_type = models.CharField(max_length=50)

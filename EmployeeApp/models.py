from django.db import models


# Create your models here.
class Employee(models.Model):
    employee_Id = models.CharField(max_length=6)
    employee_name = models.CharField(max_length=50)
    salary = models.CharField(max_length=20)

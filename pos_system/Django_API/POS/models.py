from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
# Each of these models is a table! 
# TODO: Figure out how to replace these models with the SQL

class Departments(models.Model):
    DepartmendId = models.AutoField(primary_key = True)
    DepartmentName = models.CharField(max_length=500)
    
class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key = True)
    EmployeeName= models.CharField(max_length=500)
    Department= models.CharField(max_length=500)
    DataOfJoining = models.DateField()
    PhotoFIleName = models.CharField(max_length=500)
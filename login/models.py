from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)    
    class Meta:
        db_table = 'employee_registration'
        ordering = ['id','name','department','salary','created_at']



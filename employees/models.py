from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name =models.CharField(max_length=200 ,null=False)
    last_name=models.CharField(max_length=200,null=False)
    position=models.CharField(max_length=200 ,null=False)
    department=models.CharField(max_length=200,null=False)
    employee_email=models.EmailField(max_length=200,null=False)
    performance_review=models.CharField(max_length=200,null=False)
    is_active = models.BooleanField(default=True)
    joined_created=models.DateTimeField(auto_now_add=True)

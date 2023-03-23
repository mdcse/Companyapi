from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), ('Finance', 'Finance'), ("Helthcare", 'Healthcare'), ('Education', 'Education'), ('Others', 'Other')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    possition = models.CharField(max_length=50, choices=(('CEO', 'CEO'), ('CTO', 'CTO'), ('Project Mannager', 'PM'), ('Software developer', 'SDE'), ('Other', 'Other')))


    def __str__(self):
        return self.name


from django.db import models


# Create your models here.
class MatrimonyUserReg(models.Model):
    Age_Group = (
        (9, '--------'),
        (0, '18 to 20'),
        (1, '20 to 25'),
        (2, '26 to 30'),
        (3, '31 to 35'),
        (4, '36 to 40'),
        (5, '41 to 45'),
        (6, '45 to 50'),
        (7, '50 to 55'),
        (8, '55 to 60')
    )
    Gender_Choice = (
        (0, 'Male'),
        (1, 'FeMale')
    )
    LookingFor_Choice = (
        (0, 'Groom'),
        (1, 'Bride')
    )
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Cast = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    HeadPerson = models.CharField(max_length=50)
    Degree = models.CharField(max_length=50)
    Study_Details = models.CharField(max_length=50)
    Password = models.CharField(max_length=60)
    DOB = models.DateField()
    Age = models.IntegerField(null=False, choices=Age_Group, default=" ")
    Father_PhoneNo = models.CharField(max_length=30)
    Height = models.CharField(max_length=30)
    Weight = models.CharField(max_length=30)
    Gender = models.IntegerField(null=False, choices=Gender_Choice, default=" ")
    Looking_For = models.IntegerField(null=False, choices=LookingFor_Choice, default=" ")
    Hobbies = models.CharField(null=False, max_length=300)
    Native_City = models.CharField(null=False, max_length=300)
    Current_City = models.CharField(null=False, max_length=300)
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.First_Name
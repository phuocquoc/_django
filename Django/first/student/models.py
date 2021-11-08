from django.db import models
from django.db.models.fields import EmailField


class Profile(models.Model):
    sex_choice = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='images/')
    email = models.EmailField()
    sex = models.CharField(max_length=9, choices=sex_choice, default="Female")
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

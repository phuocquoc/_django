from django.db import models

# Create your models here.


class Profile_S (models.Model):
    sexchoi = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    sex = models.CharField(max_length=10, choices=sexchoi, default='')

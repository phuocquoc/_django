from django.db import models


class Cars(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.name

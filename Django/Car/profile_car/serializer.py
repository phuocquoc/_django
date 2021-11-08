from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Cars


class CarSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = '__all__'

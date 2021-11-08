from django.db.models.base import Model
from rest_framework import serializers
from .models import Profile_S


class StudentSerilazer (serializers.ModelSerializer):
    class Meta:
        model = Profile_S
        fields = '__all__'

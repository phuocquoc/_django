import django
from django.db.models import fields
from django.forms import ModelForm, models
from django import forms
from .models import Profile, Hotel


class DateInput(forms.DateInput):
    input_type = 'date'


class Form_Student(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # birth_date = forms.DateField()

    class Meta:
        model = Profile
        # fields = ['username', 'password', 'name', 'email', 'sex']
        fields = '__all__'
        widgets = {
            'birth_date': DateInput()
        }


class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']

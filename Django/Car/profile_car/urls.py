
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateCarView.as_view(), name='index'),
]

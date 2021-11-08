from django.http import JsonResponse, response
from rest_framework.response import Response

from rest_framework import serializers, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Cars
from .serializer import CarSerializer
from rest_framework.views import APIView


class ListCreateCarView(APIView):

    def get(self, request):
        snippets = Cars.objects.all()
        serializer_class = CarSerializer(snippets, many=True)
        return Response(serializer_class.data)

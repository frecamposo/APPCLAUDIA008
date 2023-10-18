from django.shortcuts import render
from .models import Receta
from .serializers import RecetaSerializers
from rest_framework import generics
# Create your views here.

class RecetaViewSet(generics.ListCreateAPIView):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializers

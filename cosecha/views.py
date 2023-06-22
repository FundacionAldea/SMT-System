from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cosecha.models import *
from cosecha.serializers import CosechaSegSerializers


# Create your views here.
class CosechaViewSet(viewsets.ModelsViewSet):
    queryset = CosechaSeg.objects.all()
    serializer_class = CosechaSegSerializers


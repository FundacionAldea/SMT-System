from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


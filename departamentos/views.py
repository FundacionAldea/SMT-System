from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from departamentos.serializer import *
from departamentos.models import *


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = DepartamentoModel.objects.all()
    serializer_class = DepartamentoSerializer


class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = MunicipioModel.objects.all()
    serializer_class = MunicipioSerializer


class ComunidadViewSet(viewsets.ModelViewSet):
    queryset = ComunidadModel.objects.all()
    serializer_class = ComunidadSerializer
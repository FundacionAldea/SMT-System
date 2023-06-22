from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from catalogos.serializer import *
from catalogos.models import *


class AreaViewSet(viewsets.ModelViewSet):
    queryset = AreaModel.objects.all()
    serializer_class = AreaSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer


class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = ProgramasModel.objects.all()
    serializer_class = ProgramaSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = ProyectoModel.objects.all()
    serializer_class = ProyectoSerializer


class TemaViewSet(viewsets.ModelViewSet):
    queryset = TemaModel.objects.all()
    serializer_class = TemaSerializer


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = TecnicosModel.objects.all()
    serializer_class = TecnicoSerializer


class UpdateAsociadoViewSet(viewsets.ModelViewSet):
    queryset = UpdateAsociado.objects.all()
    serializer_class = UpdateAsociadoSerializer

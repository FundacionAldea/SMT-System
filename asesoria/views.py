from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from asesoria.serializers import *
from asesoria.models import *


class AsesoriaViewSet(viewsets.ModelViewSet):
    queryset = AsesoriaTecnica.objects.all()
    serializer_class = AsesoriaModelSerializer
    # permission_classes = [IsAuthenticated]


class Entrada_SalidaViewSet(viewsets.ModelViewSet):
    queryset = entradas_salidas.objects.all()
    serializer_class = EntradaSalidaSerializer
    # permission_classes = [IsAuthenticated]


class AsesoriasListView(generics.ListAPIView):
    queryset = AsesoriaTecnica.objects.all().order_by('asesoria_socio__cod').distinct('asesoria_socio__cod').reverse()
    serializer_class = AsesoriaModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_curren_user', 'conc_asesoria']
    # permission_classes = [IsAuthenticated]


class AsesoriaUltimaListView(generics.ListAPIView):
    queryset = AsesoriaTecnica.objects.filter(asesoria_socio=3)
    serializer_class = AsesoriaModelSerializer


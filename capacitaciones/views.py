from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import CapacitacionesModelSerializer, ParticipantesSerializer
from .models import Capacitaciones, Participantes_capacitacion
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class ParticipantesViewSet(viewsets.ModelViewSet):
    queryset = Participantes_capacitacion.objects.all()
    serializer_class = ParticipantesSerializer
    # permission_classes = [IsAuthenticated]


class CapacitacionesViewSet(viewsets.ModelViewSet):
    queryset = Capacitaciones.objects.all()
    serializer_class = CapacitacionesModelSerializer
    # permission_classes = [IsAuthenticated]


class CapacitacionesListView(generics.ListAPIView):
    queryset = Capacitaciones.objects.all().order_by('conc_cap')
    serializer_class = CapacitacionesModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_curren_user']
    # permission_classes = [IsAuthenticated]




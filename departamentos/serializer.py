from rest_framework import serializers
from departamentos.models import *


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartamentoModel
        fields = '__all__'
        depth = 3


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MunicipioModel
        fields = '__all__'
        depth = 1


class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunidadModel
        fields = '__all__'
        depth = 1

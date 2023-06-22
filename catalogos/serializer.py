from rest_framework import serializers
from catalogos.models import *


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoModel
        fields = '__all__'
        depth = 1


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaModel
        fields = '__all__'
        depth = 1


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramasModel
        fields = '__all__'
        depth = 1


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoModel
        fields = '__all__'
        depth = 1


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnicosModel
        fields = '__all__'
        depth = 1


class TemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemaModel
        fields = '__all__'
        depth = 1


class UpdateAsociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateAsociado
        fields = '__all__'

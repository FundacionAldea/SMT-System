from rest_framework import serializers
from .models import Capacitaciones, Participantes_capacitacion


class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participantes_capacitacion
        fields = ['cod', 'nombres_apellidos', 'cedula', 'edad', 'sexo', 'departamento', 'municipio', 'comunidad',
                  'rubro', 'manzanas_suelo', 'latitud', 'longitud', 'estado', 'fecha_asociacion', 'id_rel_capacitacion']


class CapacitacionesModelSerializer(serializers.ModelSerializer):
    participantes_capacitacion = ParticipantesSerializer(many=True)

    class Meta:
        model = Capacitaciones
        fields = ['tecnico', 'id_curren_user', 'comunidad', 'municipio', 'departamento', 'fecha', 'tema', 'programa',
                  'proyecto', 'conc_cap', 'participantes_capacitacion']

    def create(self, validated_data):
        participante = validated_data.pop('participantes_capacitacion')
        capacitacions = Capacitaciones.objects.create(**validated_data)
        for track_data in participante:
            Participantes_capacitacion.objects.create(capacitacion=capacitacions, **track_data)
        return capacitacions

    # def validate(self, data):
    #     if Capacitaciones.objects.filter(id_curren_user=data.get('id_curren_user'), conc_cap=data.get('conc_cap')).exists():
    #         raise serializers.ValidationError("Esta capacitacion ya existe")
    #     else:
    #         return data

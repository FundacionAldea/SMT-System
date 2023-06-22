from rest_framework import serializers
from asesoria.models import *


class AsociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsociadoAsesoria
        fields = ['cod', 'nombres_apellidos', 'cedula', 'edad', 'sexo', 'departamento', 'municipio', 'comunidad',
                  'rubro', 'manzanas_suelo', 'latitud', 'longitud', 'estado', 'fecha_asociacion', 'id_rel_asesoria']


class AsesoriadetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asesoriadetalles
        fields = ['area_total_finca', 'area_total_cafe', 'area_cafe_desarrollo', 'area_cafe_productivo', 'manejo_podas','diagnostico', 'analisis_suelo', 'plan_manejo', 'auditoria_interna', 'estimada_cosecha',
                  'acceso_credito', 'id_rel_asesoria', 'motivo_no_credito']


class PlagasEnfermedadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plagas_enfermedades
        fields = ['id_rel_asesoria', 'manejo_sombra', 'manejo_maleza', 'incidencia_broca', 'actracnosis', 'ojo_gallo', 'roya', 'pellejillo', 'mancha_hierro', 'bacteriosis', 'cochinilla', 'minador', 'picudo', 'derrite']


class FertilizacionEdaficaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertalizacion_edafica
        fields = ['id_rel_asesoria', 'fertilizacion_edafica', 'producto_edafico','dosis_edafica', 'estadoAPlantacionFe']


class FertilizacionFoliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertalizacion_foliar
        fields = ['id_rel_asesoria', 'fertilizacion_foliar', 'producto_foliar', 'dosis_foliar', 'estadoAPlantacionFoliar', 'medidaProdFoliar']


class EnmiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enmienda
        fields = ['id_rel_asesoria', 'fertilizacion', 'producto_enmienda', 'dosis_enmienda','estadoAPlantacionEnmienda','medidaEnmienda']


class RecomendacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = recomendaciones
        fields = ['recomendacion', 'id_rel_asesoria']




class AsesoriaModelSerializer(serializers.ModelSerializer):
    asesoria_socio = AsociadoSerializer(many=True)
    asesoria_detalle = AsesoriadetallesSerializer(many=True)
    asesoria_enfermedades_plagas = PlagasEnfermedadesSerializer(many=True)
    asesoria_edafica = FertilizacionEdaficaSerializer(many=True)
    asesoria_foliar = FertilizacionFoliarSerializer(many=True)
    asesoria_enmienda = EnmiendaSerializer(many=True)
    asesoria_recomendacion = RecomendacionesSerializer(many=True)

    class Meta:
        model = AsesoriaTecnica
        fields = ['tecnico', 'id_curren_user', 'conc_asesoria','programa', 'proyecto', 'fecha',
                  'hora', 'nombre_finca', 'etapa_fenologica', 'asesoria_socio', 'asesoria_detalle', 'asesoria_enfermedades_plagas', 'asesoria_edafica', 'asesoria_foliar', 'asesoria_enmienda','asesoria_recomendacion']

    def create(self, validated_data):
        asociado = validated_data.pop('asesoria_socio')
        asesoria_detalles = validated_data.pop('asesoria_detalle')
        plagas_enfermedades = validated_data.pop('asesoria_enfermedades_plagas')
        fertilizacion_edafica = validated_data.pop('asesoria_edafica')
        fertilizacion_foliar = validated_data.pop('asesoria_foliar')
        Enmiendas = validated_data.pop('asesoria_enmienda')
        asesoria_recomendacion = validated_data.pop('asesoria_recomendacion')
        asesoriass = AsesoriaTecnica.objects.create(**validated_data)

        for asociadoi in asociado:
            AsociadoAsesoria.objects.create(asesoria_socio=asesoriass, **asociadoi)

        for asesoria_detalless in asesoria_detalles:
            Asesoriadetalles.objects.create(asesoria_detalle=asesoriass, **asesoria_detalless)

        for plagas_enfermedade in plagas_enfermedades:
            Plagas_enfermedades.objects.create(asesoria_enfermedades_plagas=asesoriass, **plagas_enfermedade)

        for fertilizacion_edaficas in fertilizacion_edafica:
            Fertalizacion_edafica.objects.create(asesoria_edafica=asesoriass, **fertilizacion_edaficas)

        for fertilizacion_foliar in fertilizacion_foliar:
            Fertalizacion_foliar.objects.create(asesoria_foliar=asesoriass, **fertilizacion_foliar)

        for Enmiendass in Enmiendas:
            Enmienda.objects.create(asesoria_enmienda=asesoriass, **Enmiendass)

        for recomendacions in asesoria_recomendacion:
            recomendaciones.objects.create(asesoria_recomendacion=asesoriass, **recomendacions)

        return asesoriass


class EntradaSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = entradas_salidas
        fields = ['id_curren_user', 'conce_entrada_salida', 'longitud', 'latitud', 'fecha', 'hora', 'codAsociado', 'momentoMarca']
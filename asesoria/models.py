from django.db import models

class AsesoriaTecnica(models.Model):
    tecnico = models.CharField(max_length=255, verbose_name="tecnico")
    id_curren_user = models.IntegerField(default=0)
    conc_asesoria = models.IntegerField()
    programa = models.CharField(max_length=255, verbose_name="programa")
    proyecto = models.CharField(max_length=255, verbose_name="proyecto")
    fecha = models.DateField(verbose_name="fecha_asesoria")
    hora = models.TimeField(verbose_name="hora_asesoria")
    nombre_finca = models.CharField(max_length=255,verbose_name="nombre_finca")
    etapa_fenologica = models.CharField(max_length=255,verbose_name="etapa_fenologica")

    class Meta:
        unique_together = ['id_curren_user', 'conc_asesoria','fecha']

    def __int__(self):
        return self.tecnico


class AsociadoAsesoria(models.Model):
    asesoria_socio = models.ForeignKey(AsesoriaTecnica, related_name='asesoria_socio', verbose_name="asesoria_socio", on_delete=models.CASCADE)
    cod = models.IntegerField(verbose_name='cod')
    nombres_apellidos = models.CharField(max_length=255, verbose_name="nombres_y_apellidos")
    cedula = models.CharField(max_length=255, verbose_name="cedula")
    edad = models.IntegerField()
    sexo = models.CharField(max_length=15, verbose_name="sexo", default='1')
    departamento = models.CharField(max_length=255, verbose_name="departamento", default="Jinotega")
    municipio = models.CharField(max_length=100, verbose_name="departamento", default="Jinotega")
    comunidad = models.CharField(max_length=100, verbose_name="comunidad", default="Jinotega")
    rubro = models.CharField(max_length=255, verbose_name="rubro", default="otro", null=True, blank=True)
    manzanas_suelo = models.FloatField(default=0)
    latitud = models.FloatField(verbose_name="latitud", default=0.0)
    longitud = models.FloatField(verbose_name="longitud", default=0.0)
    estado = models.CharField(max_length=255, verbose_name="estado", default="")
    fecha_asociacion = models.CharField(max_length=255, verbose_name="fecha_asociacion", default="")
    id_rel_asesoria = models.IntegerField(default=0, verbose_name="id_rel_asesoria")

    class Meta:
        ordering = ['cod']

    def __str__(self):
        return '%d: %s' % (self.cod, self.nombres_apellidos)


class Asesoriadetalles(models.Model):
    asesoria_detalle = models.ForeignKey(AsesoriaTecnica, related_name='asesoria_detalle', verbose_name="asesoria_detalle", on_delete=models.CASCADE)
    area_total_finca = models.FloatField(verbose_name="area_total_finca")
    area_total_cafe = models.FloatField(verbose_name="area_total_cafe")
    area_cafe_desarrollo = models.FloatField(verbose_name="area_cafe_desarrollo")
    area_cafe_productivo = models.FloatField(verbose_name="area_cafe_productivo")
    manejo_podas = models.FloatField(verbose_name="manejo_podas")
    diagnostico = models.BooleanField(verbose_name="diagnostico")
    analisis_suelo = models.BooleanField(verbose_name="analisis_suelo")
    plan_manejo = models.BooleanField(verbose_name="plan_manejo")
    auditoria_interna = models.BooleanField(verbose_name="auditoria_interna")
    estimada_cosecha = models.BooleanField(verbose_name="estimada_cosecha")
    acceso_credito = models.BooleanField(verbose_name="acceso_credito")
    motivo_no_credito = models.CharField(max_length=255, verbose_name="motivo_no_credito")
    id_rel_asesoria = models.IntegerField(default=0, verbose_name="id_rel_asesoria")



class Plagas_enfermedades(models.Model):
    asesoria_enfermedades_plagas = models.ForeignKey(AsesoriaTecnica, related_name="asesoria_enfermedades_plagas", verbose_name="asesoria_enfermedades_plagas", on_delete=models.CASCADE)
    manejo_sombra = models.IntegerField(verbose_name="manejo_sombra")
    manejo_maleza = models.IntegerField(verbose_name="manejo_maleza")
    incidencia_broca = models.IntegerField(verbose_name="incidencia_broca")
    actracnosis = models.IntegerField(verbose_name="actracnosis")
    ojo_gallo = models.IntegerField(verbose_name="ojo_gallo")
    roya = models.IntegerField(verbose_name="roya")
    pellejillo = models.IntegerField(verbose_name="pellejillo")
    mancha_hierro = models.IntegerField(verbose_name="mancha_hierro")
    cochinilla = models.IntegerField(verbose_name="cochinilla", default=0)
    minador = models.IntegerField(verbose_name="minador", default=0)
    picudo = models.IntegerField(verbose_name="picudo", default=0)
    derrite = models.IntegerField(verbose_name="derrite", default=0)
    bacteriosis = models.IntegerField(verbose_name="bacteriosis")
    id_rel_asesoria = models.IntegerField(default=0)


class Fertalizacion_edafica(models.Model):
    asesoria_edafica = models.ForeignKey(AsesoriaTecnica, related_name="asesoria_edafica", verbose_name="asesoria_edafica", on_delete=models.CASCADE)
    fertilizacion_edafica = models.CharField(max_length=255, verbose_name="fertilizacion_edafica")
    producto_edafico = models.CharField(max_length=255, verbose_name="producto_edafico")
    estadoAPlantacionFe = models.CharField(max_length=255, verbose_name="estadoAPlantacionFe", default=0)
    dosis_edafica = models.FloatField(verbose_name="dosis_edafica")
    id_rel_asesoria = models.IntegerField(default=0)



class Fertalizacion_foliar(models.Model):
    asesoria_foliar = models.ForeignKey(AsesoriaTecnica, related_name="asesoria_foliar",verbose_name="asesoria_foliar", on_delete=models.CASCADE)
    fertilizacion_foliar = models.CharField(max_length=255, verbose_name="fertilizacion_foliar")
    estadoAPlantacionFoliar = models.CharField(max_length=255, verbose_name="estadoAPlantacionFoliar", default=0)
    producto_foliar = models.CharField(max_length=255, verbose_name="producto_foliar")
    medidaProdFoliar = models.CharField(max_length=255, verbose_name="medidaProdFoliar", default=0)
    dosis_foliar = models.FloatField(verbose_name="dosis_foliar")
    id_rel_asesoria = models.IntegerField(default=0)



class Enmienda(models.Model):
    asesoria_enmienda = models.ForeignKey(AsesoriaTecnica, related_name="asesoria_enmienda",verbose_name="asesoria_enmienda", on_delete=models.CASCADE)
    fertilizacion = models.CharField(max_length=255, verbose_name="fertilizacion_foliar")
    producto_enmienda = models.CharField(max_length=255, verbose_name="producto_enmienda")
    estadoAPlantacionEnmienda = models.CharField(max_length=255, verbose_name="estadoAPlantacionEnmienda", default=0)
    dosis_enmienda = models.FloatField(verbose_name="dosis_enmienda")
    medidaEnmienda = models.CharField(max_length=100, verbose_name="medidaEnmienda", default="Empty")
    id_rel_asesoria = models.IntegerField(default=0)



class recomendaciones(models.Model):
    asesoria_recomendacion = models.ForeignKey(AsesoriaTecnica, related_name="asesoria_recomendacion", verbose_name="asesoria_recomendacion", on_delete=models.CASCADE)
    recomendacion = models.CharField(max_length=255, verbose_name="recomendacion")
    id_rel_asesoria = models.IntegerField(default=0)


class entradas_salidas(models.Model):   # UBICACION ADAN
    id_curren_user = models.IntegerField()
    conce_entrada_salida = models.IntegerField()
    codAsociado = models.IntegerField(default=0)
    momentoMarca = models.CharField(max_length=100, default="Pendiente")
    longitud = models.FloatField(verbose_name="longitud",  default=0.0)
    latitud = models.FloatField(verbose_name="latitud", default=0.0)
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        unique_together = ['id_curren_user', 'conce_entrada_salida' ,'fecha']


from django.db import models

# Create your models here.
class CosechaSeg(models.Model):
    cod = models.IntegerField()
    nombres_apellidos = models.CharField(max_length=255, verbose_name="nombres_apellidos")
    cedula = models.CharField(max_length=255, verbose_name="cedula")
    sexo = models.CharField(max_length=15, verbose_name="sexo", default="1")
    nombre_finca = models.CharField(max_length=255, verbose_name="nombre_finca")
    comunidad = models.CharField(max_length=255, verbose_name="comunidad")
    municipio = models.CharField(max_length=255, verbose_name="comunidad")
    fecha_hora_anterior = models.DateTimeField(verbose_name="fecha_hora_anterior")
    fecha_hora_actual = models.DateTimeField(verbose_name="fecha_hora_anterior")
    nombre_tecnico = models.CharField(max_length=255, verbose_name="nombre_tecnico")
    id_curren_user = models.IntegerField(default=0)
    compromiso_entrega = models.FloatField(verbose_name="compromiso_entrega", default=0.0)
    total_entrega = models.FloatField(verbose_name="total_entrega", default=0.0)
    porcentaje_zona = models.IntegerField()
    avance_cosecha = models.FloatField(verbose_name="avance_cosecha", default=0.0)
    avance_prenda = models.FloatField(verbose_name="avance_prenda", default=0.0)




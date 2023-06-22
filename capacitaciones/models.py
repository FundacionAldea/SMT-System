from django.db import models


class Capacitaciones(models.Model):
    tecnico = models.CharField(max_length=255, verbose_name="asesor tecnico")
    id_curren_user = models.IntegerField(default=0)
    comunidad = models.CharField(max_length=255, verbose_name="comunidad")
    municipio = models.CharField(max_length=255, verbose_name="municipio")
    departamento = models.CharField(max_length=255, verbose_name="departamento")
    fecha = models.DateField(max_length=255, verbose_name="fecha")
    tema = models.CharField(max_length=255, verbose_name="tema")
    programa = models.CharField(max_length=255, verbose_name="programa")
    proyecto = models.CharField(max_length=255, verbose_name="Proyecto")
    conc_cap = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['id_curren_user', 'conc_cap']

    def __str__(self):
        return self.tema

    def save(self, *args, **kwargs):
        print("Guardando")
        super().save(*args, **kwargs)


class Participantes_capacitacion(models.Model):
    capacitacion = models.ForeignKey(Capacitaciones, related_name='participantes_capacitacion', on_delete=models.CASCADE)
    cod = models.IntegerField()
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
    id_rel_capacitacion = models.IntegerField(default=0)

    class Meta:
        ordering = ['cod']

    def __str__(self):
        return '%d: %s' % (self.cod, self.nombres_apellidos)







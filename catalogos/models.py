from django.db import models


class ProgramasModel(models.Model):
    programa = models.CharField(max_length=255, verbose_name="programa")
    nombre_abreviado = models.CharField(max_length=255, verbose_name="nombre_abreviado")
    descripcion = models.TextField(max_length=255, verbose_name="descripcion")
    fecha_inicio = models.DateField(default=0000-00-00)
    fecha_finalizacion = models.DateField(default=0000-00-00)

    def __str__(self):
        return self.programa


class ProyectoModel(models.Model):
    proyecto = models.CharField(max_length=255, verbose_name="Proyecto")
    #programa = models.ManyToManyField(ProgramasModel)
    descripcion = models.TextField(max_length=255, verbose_name="descripcion")
    presupuesto = models.FloatField(default=0.0)
    fecha_inicio = models.DateField(default=0000-00-00)
    fecha_finalizacion = models.DateField(default=0000-00-00)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.proyecto


class TemaModel(models.Model):
    tema = models.CharField(max_length=255, verbose_name="tema")
    #proyecto = models.ManyToManyField(ProyectoModel)

    def __str__(self):
        return self.tema


class AreaModel(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    descripcion = models.TextField(max_length=255, verbose_name="descripcion")
    fecha_inicio = models.DateField(default=0000-00-0)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre

class CargoModel(models.Model):
    cargo = models.CharField(max_length=255, verbose_name="cargo")
    descripcion = models.TextField(max_length=255, verbose_name="descripcion")
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.cargo

class TecnicosModel(models.Model):
    Nombres_apellidos = models.CharField(max_length=255, verbose_name="Nombres_apellidos")
    area = models.ManyToManyField(AreaModel)
    cargo = models.ManyToManyField(CargoModel)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.Nombres_apellidos


class NoAsociado(models.Model):
    nombres_apellidos = models.CharField(max_length=255, verbose_name="nombres_apellidos")
    cedula = models.CharField(max_length=255, verbose_name="nombres_apellidos")
    edad = models.IntegerField(verbose_name="edad")
    sexo = models.CharField(max_length=15, verbose_name="sexo_noasociado")
    comunidad = models.CharField(max_length=255, verbose_name="comunidad")
    municipio = models.CharField(max_length=255, verbose_name="municipio")
    departamento = models.CharField(max_length=255, verbose_name="departamento")
    padrino = models.CharField(max_length=255, verbose_name="nombres_apellidos")
    contacto = models.IntegerField( verbose_name="contacto")
    rubro = models.CharField(max_length=255, verbose_name="rubro_noasociado")


class UpdateAsociado(models.Model):
    nombre = models.CharField(max_length=255, verbose_name="nombre")
    cedula = models.CharField(max_length=14, verbose_name="cedula")
    edad = models.IntegerField(verbose_name="edad")
    fecha_asociacion= models.DateField(verbose_name="fecha_asociacion")
    sexo = models.CharField(max_length=255, verbose_name="sexo")
    comunidad = models.CharField(max_length=255, verbose_name="comunidad")
    municipio = models.CharField(max_length=255, verbose_name="municipio")
    departamento = models.CharField(max_length=255, verbose_name="departamento")
    latitud = models.FloatField(verbose_name="latitud")
    longitud = models.FloatField(verbose_name="longitud")
    rubros = models.CharField(max_length=100, verbose_name="rubros")
    manzanas_suelos = models.IntegerField(verbose_name="manzanas_suelos")
    num_update = models.IntegerField(verbose_name="num_update")
    actualizado = models.BooleanField(verbose_name="actualizado")
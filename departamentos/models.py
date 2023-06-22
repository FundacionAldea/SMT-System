from django.db import models

class ComunidadModel(models.Model):
    comunidad = models.CharField(max_length=255)

    def __str__(self):
        return self.comunidad

class MunicipioModel(models.Model):
    municipio= models.CharField(max_length=255, verbose_name="municipio")
    comunidad = models.ManyToManyField(ComunidadModel)

    def __str__(self):
        return self.municipio


class DepartamentoModel(models.Model):
    departamento = models.CharField(max_length=255, verbose_name="departamento")
    municipio = models.ManyToManyField(MunicipioModel)

    def __str__(self):
        return self.departamento


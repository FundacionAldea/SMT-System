from django.db import models


class beneficioModel(models.Model):
    beneficio = models.CharField(max_length=255, verbose_name="beneficio")
    creado = models.DateField(auto_now=True)

    def __str__(self):
        return self.beneficio
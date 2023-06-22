from django.contrib import admin
from asesoria.models import *


class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(AsesoriaTecnica)
    admin.site.register(Asesoriadetalles)
    admin.site.register(Plagas_enfermedades)
    admin.site.register(Fertalizacion_edafica)
    admin.site.register(Fertalizacion_foliar)
    admin.site.register(AsociadoAsesoria)
    admin.site.register(Enmienda)
    admin.site.register(recomendaciones)
    admin.site.register(entradas_salidas)

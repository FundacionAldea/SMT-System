from django.contrib import admin
from departamentos.models import *

class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(DepartamentoModel),
    admin.site.register(MunicipioModel),
    admin.site.register(ComunidadModel),
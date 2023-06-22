from django.contrib import admin
from catalogos.models import *

class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(CargoModel)
    admin.site.register(ProyectoModel)
    admin.site.register(TemaModel)
    admin.site.register(ProgramasModel)
    admin.site.register(TecnicosModel)
    admin.site.register(AreaModel)
    admin.site.register(UpdateAsociado)

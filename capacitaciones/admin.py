from django.contrib import admin
from capacitaciones.models import Capacitaciones, Participantes_capacitacion


class AuthorAdmin(admin.ModelAdmin):
    pass
    admin.site.register(Capacitaciones)
    admin.site.register(Participantes_capacitacion)
# Register your models here.


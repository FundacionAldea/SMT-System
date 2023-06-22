from django.contrib import admin
from recursos.models import *

class AuthorAdmin(admin.ModelAdmin):
    admin.site.register(beneficioModel),
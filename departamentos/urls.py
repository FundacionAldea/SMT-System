import django.urls
from django.urls import path, include
from departamentos.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("departamento", DepartamentoViewSet, basename="departamento")
router.register("municipio", MunicipioViewSet, basename="municipio")
router.register("comunidad", ComunidadViewSet, basename="comunidad")

urlpatterns = [
    path('', include(router.urls))
]

import django.urls
from django.urls import path, include
from catalogos.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("cargo", CargoViewSet, basename="cargo")
router.register("programa", ProgramaViewSet, basename="programa")
router.register("area", AreaViewSet, basename="area")
router.register("proyecto", ProyectoViewSet, basename="proyecto")
router.register("tecnicos", TecnicoViewSet, basename="tecnicos")
router.register("tema", TemaViewSet, basename="tema")
router.register("updateAsociado", UpdateAsociadoViewSet, basename="updateAsociado")

urlpatterns = [
    path('', include(router.urls))
]

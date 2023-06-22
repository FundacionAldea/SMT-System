import django.urls
from django.urls import path, include
from asesoria.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("asesoria", AsesoriaViewSet, basename="asesoria")
router.register("marcaje", Entrada_SalidaViewSet, basename="marcaje")

urlpatterns = [
    path('', include(router.urls)),
    path('list', AsesoriasListView.as_view()),
    path('list2', AsesoriaUltimaListView.as_view()),

]

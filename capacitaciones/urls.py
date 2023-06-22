import django.urls
from django.urls import path, include
from capacitaciones.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("capacitaciones", CapacitacionesViewSet, basename="capacitaciones")
router.register("participantes", ParticipantesViewSet, basename="participantes")

urlpatterns = [
    path('', include(router.urls)),
    path('list', CapacitacionesListView.as_view()),
]

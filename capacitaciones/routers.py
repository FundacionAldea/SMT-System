from rest_framework.routers import DefaultRouter
from capacitaciones.views import CapacitacionesViewSet, ParticipantesViewSet

router = DefaultRouter()
router.register(r'capacitacion', CapacitacionesViewSet)

for r in router.urls:
    print(r)
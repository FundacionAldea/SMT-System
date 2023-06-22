from rest_framework.routers import DefaultRouter
from asesoria.views import *

router = DefaultRouter()
router.register(r'capacitacion', AsesoriaViewSet)

for r in router.urls:
    print(r)
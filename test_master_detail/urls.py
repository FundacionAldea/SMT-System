import django.urls
from django.urls import path, include
from test_master_detail.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("album", AlbumViewSet, basename="album")

urlpatterns = [
    path('', include(router.urls)),
]

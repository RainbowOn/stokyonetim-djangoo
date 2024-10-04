from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusteriKayitViewSet

router = DefaultRouter()
router.register(r'kayitlar', MusteriKayitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

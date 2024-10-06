# envanter/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MusteriKayitViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'kayitlar', MusteriKayitViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),  # Özel Token Auth endpoint'i
]

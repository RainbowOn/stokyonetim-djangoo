import logging
from .models import MusteriKayit
from .serializers import MusteriKayitSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


logger = logging.getLogger(__name__)

class MusteriKayitViewSet(viewsets.ModelViewSet):
    queryset = MusteriKayit.objects.all()
    serializer_class = MusteriKayitSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Sadece kimliği doğrulanmış kullanıcılar değişiklik yapabilir
    authentication_classes = [TokenAuthentication] # Token tabanlı kimlik doğrulama kullan

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Müşteri kaydını oluşturan kullanıcıyı kaydet

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
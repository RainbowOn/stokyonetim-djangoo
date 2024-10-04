# envanter/views.py

import logging
from .models import MusteriKayit
from .serializers import MusteriKayitSerializer
from rest_framework import viewsets


logger = logging.getLogger(__name__)

class MusteriKayitViewSet(viewsets.ModelViewSet):
    queryset = MusteriKayit.objects.all()
    serializer_class = MusteriKayitSerializer

    def perform_create(self, serializer):
        logger.info("Yeni kayıt oluşturuluyor...")
        try:
            serializer.save()
            logger.info("Kayıt başarıyla kaydedildi.")
        except Exception as e:
            logger.error(f"Kayıt kaydedilemedi: {e}")

    # perform_create metodunu kaldırıyoruz çünkü model save metodunda raf_numarasi'yı otomatik olarak atıyor

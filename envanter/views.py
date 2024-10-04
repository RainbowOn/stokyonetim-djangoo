# envanter/views.py

import logging
from .models import MusteriKayit
from .serializers import MusteriKayitSerializer
from rest_framework import viewsets

logger = logging.getLogger(__name__)

class MusteriKayitViewSet(viewsets.ModelViewSet):
    queryset = MusteriKayit.objects.all()
    serializer_class = MusteriKayitSerializer

    # perform_create metodunu kaldırıyoruz çünkü model save metodunda raf_numarasi'yı otomatik olarak atıyor

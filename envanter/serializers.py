from rest_framework import serializers
from .models import MusteriKayit

class MusteriKayitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusteriKayit
        fields = '__all__'
        read_only_fields = ('raf_numarasi', 'durum', 'id')

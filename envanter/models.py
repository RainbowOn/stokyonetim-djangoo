# envanter/models.py

from django.db import models
import random


class MusteriKayit(models.Model):
    isim = models.CharField(max_length=100, null=True, blank=True)
    soyisim = models.CharField(max_length=100, null=True, blank=True)
    firma_adi = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    telefon_numarasi = models.CharField(max_length=10)
    arac_plakasi = models.CharField(max_length=20, null=True, blank=True)
    urun_adi = models.CharField(max_length=100)
    urun_markasi = models.CharField(max_length=100)
    urun_ebadi = models.CharField(max_length=50)
    urun_tipi = models.CharField(
        max_length=50,
        choices=[
            ('Yazlık', 'Yazlık'),
            ('Kışlık', 'Kışlık'),
            ('Dört Mevsim', 'Dört Mevsim')
        ]
    )
    adet = models.PositiveIntegerField()
    depo_bilgisi = models.CharField(max_length=100)
    not_field = models.TextField(null=True, blank=True)
    raf_numarasi = models.PositiveIntegerField(unique=True, blank=True, null=True)  # Sadece sayısal değer alacak
    durum = models.CharField(max_length=50, default="Aktif")
    
    ikinci_urun_adi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_markasi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_ebadi = models.CharField(max_length=50, null=True, blank=True)
    ikinci_urun_adet = models.PositiveIntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.raf_numarasi:
            self.raf_numarasi = self.generate_unique_raf_numarasi()
        super().save(*args, **kwargs)

    def generate_unique_raf_numarasi(self):
        while True:
            # Benzersiz sayısal bir değer oluşturur
            raf_numarasi = random.randint(1, 999999)
            if not MusteriKayit.objects.filter(raf_numarasi=raf_numarasi).exists():
                return raf_numarasi

import uuid
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MusteriKayit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # settings.AUTH_USER_MODEL kullanımı
    isim = models.CharField(max_length=100, null=True, blank=True)
    soyisim = models.CharField(max_length=100, null=True, blank=True)
    firma_adi = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    telefon_numarasi = PhoneNumberField(null=True, blank=True)
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
    raf_numarasi = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    durum = models.CharField(max_length=50, default="Aktif")

    ikinci_urun_adi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_markasi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_ebadi = models.CharField(max_length=50, null=True, blank=True)
    ikinci_urun_adet = models.PositiveIntegerField(null=True, blank=True)

    kayit_tarihi = models.DateTimeField(auto_now_add=True)

    geri_sayim = models.IntegerField(blank=True, null=True, editable=True)

    def save(self, *args, **kwargs):
        # İlk kayıt olduğunda geri sayımı 365 gün olarak ayarla
        if self.geri_sayim is None:
            self.geri_sayim = 365
        super().save(*args, **kwargs)

    @property
    def geri_sayim_gun(self):
        gecen_gun_sayisi = (datetime.now() - self.kayit_tarihi).days
        return 365 - gecen_gun_sayisi

    def __str__(self):
        if self.isim and self.soyisim:
            return f"{self.isim} {self.soyisim}"
        elif self.firma_adi:
            return self.firma_adi
        else:
            return f"Müşteri {self.id}"


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
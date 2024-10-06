import uuid
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    def create_user(self, email, isim, password=None, **extra_fields):
        """
        Normal kullanıcı oluşturmak için metod.
        """
        if not email:
            raise ValueError('Kullanıcı için email adresi girmelisiniz.')
        if not isim:
            raise ValueError('Kullanıcı için isim girmelisiniz.')
        email = self.normalize_email(email)
        user = self.model(email=email, isim=isim, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, isim, password=None, **extra_fields):
        """
        Süper kullanıcı oluşturmak için metod.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Süper kullanıcı için is_staff=True olmalıdır.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Süper kullanıcı için is_superuser=True olmalıdır.')

        return self.create_user(email, isim, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # username alanını kaldırıyoruz
    email = models.EmailField(unique=True)
    isim = models.CharField(max_length=100)
    soyisim = models.CharField(max_length=100, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['isim']  # Süper kullanıcı oluştururken gereksinim duyulan ek alanlar

    objects = CustomUserManager()

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.email

class MusteriKayit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    isim = models.CharField(max_length=100, blank=True, null=True)
    soyisim = models.CharField(max_length=100, blank=True, null=True)
    firma_adi = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    telefon_numarasi = PhoneNumberField(blank=True)
    
    arac_plakasi = models.CharField(max_length=20, blank=True, null=True)
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
    depo_bilgisi = models.CharField(max_length=100)  # depo_bilgisi zorunlu
    not_field = models.TextField(null=True, blank=True)
    raf_numarasi = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    durum = models.CharField(max_length=50, default="Aktif")
    
    ikinci_urun_adi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_markasi = models.CharField(max_length=100, null=True, blank=True)
    ikinci_urun_ebadi = models.CharField(max_length=50, null=True, blank=True)
    ikinci_urun_adet = models.PositiveIntegerField(null=True, blank=True)
    ikinci_urun_varmi = models.BooleanField(default=False)
    
    kayit_tarihi = models.DateTimeField(auto_now_add=True)
    geri_sayim = models.IntegerField(blank=True, null=True, editable=True)
    
    def save(self, *args, **kwargs):
        if self.geri_sayim is None:
            self.geri_sayim = 365
        self.full_clean()
        super().save(*args, **kwargs)
    
    @property
    def geri_sayim_gun(self):
        gecen_gun_sayisi = (datetime.now().date() - self.kayit_tarihi.date()).days
        return 365 - gecen_gun_sayisi
    
    def clean(self):
        if not (self.isim and self.soyisim) and not self.firma_adi:
            raise ValidationError("İsim ve soyisim veya firma adı zorunludur.")
        
        if self.ikinci_urun_varmi and not (self.ikinci_urun_adi and self.ikinci_urun_markasi and self.ikinci_urun_ebadi and self.ikinci_urun_adet):
            raise ValidationError("İkinci ürün bilgileri eksik.")
    
    def __str__(self):
        if self.isim and self.soyisim:
            return f"{self.isim} {self.soyisim}"
        elif self.firma_adi:
            return self.firma_adi
        else:
            return f"Müşteri {self.id}"

from django import forms
from django.contrib import admin
from .models import MusteriKayit

class MusteriKayitForm(forms.ModelForm):
    ikinci_urun_varmi = forms.BooleanField(required=False)

    class Meta:
        model = MusteriKayit
        fields = '__all__'  # veya istediğiniz alanları listeleyin

    def clean(self):
        cleaned_data = super().clean()
        ikinci_urun_varmi = cleaned_data.get("ikinci_urun_varmi")

        if ikinci_urun_varmi:
            ikinci_urun_adi = cleaned_data.get("ikinci_urun_adi")
            ikinci_urun_markasi = cleaned_data.get("ikinci_urun_markasi")
            ikinci_urun_ebadi = cleaned_data.get("ikinci_urun_ebadi")
            ikinci_urun_adet = cleaned_data.get("ikinci_urun_adet")

            if not all([ikinci_urun_adi, ikinci_urun_markasi, ikinci_urun_ebadi, ikinci_urun_adet]):
                raise forms.ValidationError("İkinci ürün bilgileri eksik.")

# Admin.py'de formu belirtin
class MusteriKayitAdmin(admin.ModelAdmin):
    form = MusteriKayitForm
    list_display = ('isim', 'soyisim', 'firma_adi', 'user', 'raf_numarasi', 'kayit_tarihi', 'geri_sayim')
    search_fields = ('isim', 'soyisim', 'firma_adi', 'arac_plakasi', 'raf_numarasi')
    readonly_fields = ('kayit_tarihi', 'geri_sayim')  # Bu alanları salt okunur yap

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(MusteriKayit, MusteriKayitAdmin)

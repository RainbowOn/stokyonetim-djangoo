from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth import get_user_model

from .models import CustomUser, MusteriKayit  # CustomUser modelinizi import edin


class LogEntryAdmin(admin.ModelAdmin):
    # ... (LogEntry için istediğiniz diğer özelleştirmeler) ...

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = get_user_model().objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(LogEntry, LogEntryAdmin)


class MusteriKayitAdmin(admin.ModelAdmin):
    list_display = ('isim', 'soyisim', 'firma_adi', 'user', 'raf_numarasi', 'kayit_tarihi', 'geri_sayim')
    search_fields = ('isim', 'soyisim', 'firma_adi', 'arac_plakasi', 'raf_numarasi')
    readonly_fields = ('kayit_tarihi', 'geri_sayim')  # Bu alanları salt okunur yap

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


admin.site.register(MusteriKayit, MusteriKayitAdmin)
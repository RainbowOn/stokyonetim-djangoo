from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MusteriKayit

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'isim', 'soyisim', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')
    search_fields = ('email', 'isim', 'soyisim')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Kişisel Bilgiler', {'fields': ('isim', 'soyisim')}),
        ('İzinler', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Tarihler', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'isim', 'soyisim', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

class MusteriKayitAdmin(admin.ModelAdmin):
    list_display = ('isim', 'soyisim', 'firma_adi', 'user', 'raf_numarasi', 'kayit_tarihi', 'geri_sayim_gun')
    search_fields = ('isim', 'soyisim', 'firma_adi', 'arac_plakasi', 'raf_numarasi')
    readonly_fields = ('kayit_tarihi', 'geri_sayim_gun')  # Bu alanları salt okunur yap

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

admin.site.register(MusteriKayit, MusteriKayitAdmin)

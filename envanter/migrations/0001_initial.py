# Generated by Django 5.1.1 on 2024-10-05 22:28

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='MusteriKayit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(blank=True, max_length=100, null=True)),
                ('soyisim', models.CharField(blank=True, max_length=100, null=True)),
                ('firma_adi', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefon_numarasi', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('arac_plakasi', models.CharField(blank=True, max_length=20, null=True)),
                ('urun_adi', models.CharField(max_length=100)),
                ('urun_markasi', models.CharField(max_length=100)),
                ('urun_ebadi', models.CharField(max_length=50)),
                ('urun_tipi', models.CharField(choices=[('Yazlık', 'Yazlık'), ('Kışlık', 'Kışlık'), ('Dört Mevsim', 'Dört Mevsim')], max_length=50)),
                ('adet', models.PositiveIntegerField()),
                ('depo_bilgisi', models.CharField(max_length=100)),
                ('not_field', models.TextField(blank=True, null=True)),
                ('raf_numarasi', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('durum', models.CharField(default='Aktif', max_length=50)),
                ('ikinci_urun_adi', models.CharField(blank=True, max_length=100, null=True)),
                ('ikinci_urun_markasi', models.CharField(blank=True, max_length=100, null=True)),
                ('ikinci_urun_ebadi', models.CharField(blank=True, max_length=50, null=True)),
                ('ikinci_urun_adet', models.PositiveIntegerField(blank=True, null=True)),
                ('ikinci_urun_varmi', models.BooleanField(default=False)),
                ('kayit_tarihi', models.DateTimeField(auto_now_add=True)),
                ('geri_sayim', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# envanter/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MusteriKayit

User = get_user_model()

class MusteriKayitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusteriKayit
        fields = '__all__'
        read_only_fields = ('raf_numarasi', 'durum', 'id')

    def validate_adet(self, value):
        if value <= 0:
            raise serializers.ValidationError("Adet 0'dan büyük olmalıdır.")
        return value

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label="Email", write_only=True)
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, write_only=True)
    token = serializers.CharField(label="Token", read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError("Invalid email or password.")

            if not user.check_password(password):
                raise serializers.ValidationError("Invalid email or password.")

            if not user.is_active:
                raise serializers.ValidationError("User account is disabled.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password'.")

        attrs['user'] = user
        return attrs

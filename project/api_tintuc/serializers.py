from .models import Giaidau,Tintuc
from rest_framework import serializers


class GiaidauSerializers(serializers.ModelSerializer):
    class Meta:
        model = Giaidau
        fields="__all__"

class TintucSerializers(serializers.ModelSerializer):
    giaidau = serializers.SlugRelatedField(
        queryset=Giaidau.objects.all(), slug_field="tenGD"
    )
    class Meta:
        model = Tintuc
        fields ="__all__"
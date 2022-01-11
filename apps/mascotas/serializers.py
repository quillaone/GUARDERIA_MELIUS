from rest_framework import serializers
from .models import Mascota


class MascotaSerializers(serializers.ModelSerializer):
    class Meta():
        model = Mascota
        fields = '__all__'

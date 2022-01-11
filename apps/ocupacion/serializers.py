from rest_framework import serializers
from .models import Reservacion
from apps.mascotas.serializers import MascotaSerializers


class ReservationSerializers(serializers.ModelSerializer):
    mascotas = MascotaSerializers(read_only=True, many=True)

    class Meta:
        model = Reservacion
        fields = '__all__'

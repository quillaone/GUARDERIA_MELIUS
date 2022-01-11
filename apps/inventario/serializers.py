from rest_framework import serializers
from .models import Empleado, RegistroArticulo, Articulo


class ArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'

class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class RegistroArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroArticulo
        fields = '__all__'
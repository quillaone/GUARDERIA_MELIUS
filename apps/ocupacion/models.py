from django.db import models
from apps.mascotas.models import Mascota


class Reservacion(models.Model):
    nombre = models.ForeignKey(Mascota, to_field='id', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200, null=False)
    fecha_reserva = models.DateField(null=True, default=None, blank=True)

    class Meta:
        db_table = 'reservacion_citas'

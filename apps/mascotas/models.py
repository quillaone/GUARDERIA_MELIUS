from django.db import models


class Mascota(models.Model):
    nombre = models.CharField(max_length=200, null=False)
    tipo = models.CharField(max_length=200)
    edad = models.CharField(max_length=100)
    propietario = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'mascotas'

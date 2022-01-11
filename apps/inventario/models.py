from django.db import models


class Articulo(models.Model):
    name_articulo = models.CharField(max_length=200)

    class Meta:
        db_table = 'inventario_articulo'


class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telefono = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)

    class Meta:
        db_table = 'empleado'


class RegistroArticulo(models.Model):
    name_articulo = models.ForeignKey(Articulo, to_field='id', on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, to_field='id', on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    date_use = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        db_table = 'registro_articulo'

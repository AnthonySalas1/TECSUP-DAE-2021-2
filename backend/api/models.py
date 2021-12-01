from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
        
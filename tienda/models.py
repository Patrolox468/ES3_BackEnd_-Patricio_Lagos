from .utils import formato_clp
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nombre

class Juego(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="juegos"
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to="juegos/")
    precio = models.PositiveIntegerField()
    jugadores = models.CharField(max_length=50)
    edad_minima= models.PositiveSmallIntegerField()
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    @property
    def precio_clp(self):
        return formato_clp(self.precio)

    def __str__(self):
        return self.nombre
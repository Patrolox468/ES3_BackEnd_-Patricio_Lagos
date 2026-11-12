from .utils import formato_clp
from django.db import models
import uuid

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

class Pedido(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="pedidos")
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    cantidad = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    codigo = models.CharField(max_length=8, unique=True, editable=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            self.codigo = uuid.uuid4().hex[:8].upper()
        super().save(*args, **kwargs)

    @property
    def total(self):
        return self.juego.precio * self.cantidad

    @property
    def total_clp(self):
        return formato_clp(self.total)

    def __str__(self):
        return f"Pedido {self.codigo} - {self.nombre}"
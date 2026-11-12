from django.contrib import admin
from .models import Categoria, Juego, Pedido
from .utils import formato_clp

admin.site.register(Categoria)

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "disponible", "stock", "precio_en_pesos")
    list_filter = ("categoria", "disponible")
    search_fields = ("nombre",)

    @admin.display(description="Precio", ordering="precio")
    def precio_en_pesos(self, obj):
        return formato_clp(obj.precio)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("codigo", "juego", "nombre", "cantidad", "fecha")
    list_filter = ("juego",)
    search_fields = ("nombre", "correo")
from django.shortcuts import render
from .models import Juego


def catalogo(request):
    juegos = Juego.objects.filter(disponible=True).select_related("categoria")
    return render(request, "tienda/catalogo.html", {"juegos": juegos})
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Juego


def detalle(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id, disponible=True)
    return render(request, "tienda/detalle.html", {"juego": juego})


def catalogo(request):
    juegos = Juego.objects.filter(disponible=True).select_related("categoria")

    q = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria", "")

    if q:
        juegos = juegos.filter(nombre__icontains=q)

    if categoria_id.isdigit():
        categoria_id = int(categoria_id)
        juegos = juegos.filter(categoria_id=categoria_id)
    else:
        categoria_id = None

    contexto = {
        "juegos": juegos,
        "categorias": Categoria.objects.all(),
        "q": q,
        "categoria_id": categoria_id,
    }
    return render(request, "tienda/catalogo.html", contexto)
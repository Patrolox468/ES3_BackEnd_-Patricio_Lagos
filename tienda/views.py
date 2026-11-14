from django.shortcuts import render, get_object_or_404, redirect
from .forms import PedidoForm
from .models import Categoria, Juego


def detalle(request, juego_id):
    juego = get_object_or_404(Juego, id=juego_id, disponible=True)
    if request.method == "POST" and juego.stock > 0:
        form = PedidoForm(request.POST, juego=juego)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.juego = juego
            pedido.save()
            juego.stock -= pedido.cantidad
            juego.save()
            return redirect("detalle", juego_id=juego.id)
    else:
        form = PedidoForm(juego=juego)
    return render(request, "tienda/detalle.html", {"juego": juego, "form": form})

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
from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Pedido
        fields = ["nombre", "correo", "telefono", "cantidad"]
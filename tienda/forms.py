from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Pedido
        fields = ["nombre", "correo", "telefono", "cantidad"]

    def __init__(self, *args, juego=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.juego = juego

    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if self.juego and cantidad > self.juego.stock:
            raise forms.ValidationError(
                f"Solo hay {self.juego.stock} unidades disponibles."
            )
        return cantidad
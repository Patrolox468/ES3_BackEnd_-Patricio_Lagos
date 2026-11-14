from django.urls import path
from . import views

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("juego/<int:juego_id>/", views.detalle, name="detalle"),
    path("comprobante/<str:codigo>/", views.comprobante, name="comprobante"),
]
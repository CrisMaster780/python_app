from django.urls import path
from .views import cliente_index, nuevo_cliente, modificar_cliente, eliminar_cliente

urlpatterns = [
    path("", cliente_index, name="clientes"),
    path("nuevo_cliente/", nuevo_cliente, name="nuevo_cliente"),
    path("modificar_cliente/<int:id>/", modificar_cliente, name="modificar_cliente"),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name='eliminar_cliente'),
]


from django.urls import path
from .views import productos_index, nuevo_producto
urlpatterns = [
    path('', productos_index, name='productos'),
    path('nuevo_producto/', nuevo_producto, name='nuevo_producto'),
  
]
"""  path('nuevo_cliente/', nuevo_cliente, name='nuevo_cliente'),
    path('modificar_cliente/<int:id>/', modificar_cliente, name='modificar_cliente'),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name='eliminar_cliente'), """
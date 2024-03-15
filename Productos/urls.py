from django.urls import path
from .views import productos_index, nuevo_producto, modificar_producto, eliminar_producto
urlpatterns = [
    path('', productos_index, name='productos'),
    path('nuevo_producto/', nuevo_producto, name='nuevo_producto'),
    path('modificar_producto/<int:id>/', modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
  
]

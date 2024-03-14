from django.urls import path
from .views import cliente_index
urlpatterns = [
    path('', cliente_index, name='productos'),
    
  
]
"""  path('cliente_index/', cliente_index, name='cliente_index'),
    path('modificar_producto/<int:id>/', modificar_producto, name='modificar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'), """
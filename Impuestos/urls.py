from django.urls import path
from .views import impuesto_index, nuevo_impuesto, modificar_impuesto, eliminar_impuesto
urlpatterns = [
    path('', impuesto_index, name='impuestos'),
    path('nuevo_impuesto/', nuevo_impuesto, name='nuevo_impuesto'),
    path('modificar_impuesto/<int:id>/', modificar_impuesto, name='modificar_impuesto'),
    path('eliminar_impuesto/<int:id>/', eliminar_impuesto, name='eliminar_impuesto'),
]
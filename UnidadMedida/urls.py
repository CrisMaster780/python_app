from django.urls import path
from .views import unidad_medida_index, nueva_unidad_medida, modificar_unidad_medida, eliminar_unidad_medida
urlpatterns = [
    path('', unidad_medida_index, name='unidad_medida'),
    path('nueva_unidad_medida/', nueva_unidad_medida, name='nueva_unidad_medida'),
    path('modificar_unidad_medida/<int:id>/', modificar_unidad_medida, name='modificar_unidad_medida'),
    path('eliminar_unidad_medida/<int:id>/', eliminar_unidad_medida, name='eliminar_unidad_medida'),
]
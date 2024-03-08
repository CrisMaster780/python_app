from django.urls import path
from .views import clasificacion_index, nueva_clasificacion, modificar_clasificacion, eliminar_clasificacion
urlpatterns = [
    path('', clasificacion_index, name='clasificaciones'),
    path('nueva_clasificacion/', nueva_clasificacion, name='nueva_clasificacion'),
    path('modificar_clasificacion/<int:id>/', modificar_clasificacion, name='modificar_clasificacion'),
    path('eliminar_clasificacion/<int:id>/', eliminar_clasificacion, name='eliminar_clasificacion'),
]
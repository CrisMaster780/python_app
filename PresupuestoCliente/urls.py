from django.urls import path
from .views import crearPresupuesto , index_presupuesto, detallePresupuesto

urlpatterns = [
    path('', index_presupuesto, name='presupuesto'),
    path('crearPresupuesto/', crearPresupuesto, name='crear_presupuesto'),
     path('detallePresupuesto/<int:id>/', detallePresupuesto, name='detallePresupuesto'),
   
]
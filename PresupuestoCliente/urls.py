from django.urls import path
from .views import crearPresupuesto , index_presupuesto

urlpatterns = [
    path('', index_presupuesto, name='presupuesto'),
    path('crearPresupuesto/', crearPresupuesto, name='crear_presupuesto'),
   
]
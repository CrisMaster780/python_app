from django.urls import path
from .views import crearPresupuesto, index_presupuesto, detallePresupuesto, obtenerPrecioUnitario

urlpatterns = [
    path("", index_presupuesto, name="presupuesto"),
    path("crearPresupuesto/", crearPresupuesto, name="crear_presupuesto"),
    path("detallePresupuesto/<int:id>/", detallePresupuesto, name="detallePresupuesto"),
    path("obtenerPrecioUnitario/<int:id_producto>/", obtenerPrecioUnitario, name="obtenerPrecioUnitario"),
]

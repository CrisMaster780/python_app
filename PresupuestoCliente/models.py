from django.db import models
from Clientes.models import Clientes
from Productos.models import Productos

class PresupuestoCliente(models.Model):
    cliente =  models.ForeignKey(Clientes, on_delete = models.PROTECT)
    fecha = models.DateTimeField(blank = True, null = True)
    total_presupuesto = models.FloatField()
    estado_presupuesto = models.CharField(max_length=1, default = 'P')
    iva_10 = models.FloatField(null = True, blank= True)
    iva_5= models.FloatField(null = True, blank= True)
    exentas= models.FloatField(null = True, blank= True)
    estado = models.BooleanField(default = True)
    


class DetallePresupuestoCliente(models.Model):
    presupuesto = models.ForeignKey(PresupuestoCliente, on_delete= models.PROTECT)
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    precio_unitario = models.FloatField()
    iva = models.FloatField(null = True, blank= True)
    cantidad = models.PositiveIntegerField()
    total_linea = models.FloatField()

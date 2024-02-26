from django.db import models
from Clientes.models import Clientes

class PresupuestoCliente(models.Model):
    cliente =  models.ForeignKey(Clientes, on_delete = models.PROTECT)
    fecha = models.DateTimeField(blank = True, null = True)
    total_presupuesto = models.FloatField()
    estado_presupuesto = models.CharField(max_length=1, default = 'P')
    estado = models.BooleanField(default = True)


class DetallePresupuestoCliente(models.Model):
    presupuesto = models.ForeignKey(PresupuestoCliente, on_delete= models.PROTECT)
    producto = models.CharField(max_length = 250)
    precio_unitario = models.FloatField()
    cantidad = models.PositiveIntegerField()
    total_linea = models.FloatField()

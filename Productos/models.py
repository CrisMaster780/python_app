from django.db import models
from Clasificaciones.models import Clasificaciones
from Impuestos.models import Impuestos

from UnidadMedida.models import UnidadMedida

class Productos(models.Model):
    descripcion =  models.CharField(max_length = 250)
    codigo_barra = models.CharField(max_length = 250, null= True, blank = True)
    codigo_remitido = models.CharField(max_length = 250, null= True, blank = True)
    precio_costo =  models.FloatField()
    precio_venta = models.FloatField()
    precio_mayorista =  models.FloatField()
    existencia = models.IntegerField()
    clasificacion =models.ForeignKey(Clasificaciones, on_delete = models.PROTECT)
    impuesto = models.ForeignKey(Impuestos, on_delete = models.PROTECT)
    unidad_medida =  models.ForeignKey(UnidadMedida, on_delete = models.PROTECT) 
    estado = models.IntegerField(default = 1, null= True, blank = True)
    def __str__(self):
        return f"{self.descripcion} - Cod. Barra: {self.codigo_barra}  "
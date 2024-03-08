from django.db import models
from Impuestos.models import Impuestos
from Clasificaciones.models import Clasificaciones
from UnidadMedida.models import UnidadMedida

class Productos(models.Model):
    descripcion =  models.CharField(max_length = 250)
    codigo_barra = models.CharField(max_length = 250)
    codigo_remitido = models.CharField(max_length = 250)
    precio_costo =  models.FloatField()
    precio_venta = models.FloatField()
    precio_mayorista =  models.FloatField()
    existencia = models.IntegerField()
    impuesto = models.ForeignKey(Impuestos, on_delete = models.PROTECT)
    clasificacion =models.ForeignKey(Clasificaciones, on_delete = models.PROTECT)
    unidad_medida =  models.ForeignKey(UnidadMedida, on_delete = models.PROTECT)
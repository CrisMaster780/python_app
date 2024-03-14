from django.db import models


class Clientes(models.Model):
    nombre =  models.CharField(max_length = 250)
    apellido = models.CharField(max_length = 250)
    direccion = models.CharField(max_length = 250)
    telefono =  models.CharField(max_length = 250)
    correo = models.CharField(max_length = 250)
    documento =  models.CharField(max_length = 250)
    observacion = models.CharField(max_length = 250)
    estado = models.IntegerField(default = 1, null= True, blank = True)
from django.db import models


class Impuestos(models.Model):
    descripcion =  models.CharField(max_length = 250)
    porcentaje = models.FloatField()
    estado = models.IntegerField(default = 1, null= True, blank = True)
    def __str__(self):
        return f"{self.descripcion} - {self.porcentaje}"
    
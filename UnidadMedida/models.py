from django.db import models


class UnidadMedida(models.Model):
    descripcion =  models.CharField(max_length = 250)
    resumido = models.CharField(max_length = 250)
    estado = models.IntegerField(default = 1, null= True, blank = True)
    def __str__(self):
        return self.descripcion
    
from django.db import models

class UnidadMedida(models.Model):
    descripcion = models.CharField(max_length = 250)
    resumido = models.CharField(max_length = 250 , null =True, blank = True)
    estado = models.IntegerField(default= 1, null=True, blank = True)
    
    def __str__(self):
        return f"{self.descripcion}"

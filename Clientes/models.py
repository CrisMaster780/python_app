from django.db import models

class Clientes(models.Model):
    nombre =  models.CharField(max_length = 250)
    apellido = models.CharField(max_length = 250)
    documento = models.CharField(max_length = 250, unique=True)
    direccion =  models.CharField(max_length = 250)
    telefono = models.CharField(max_length = 250)
    correo =  models.CharField(max_length = 250)
    observacion =  models.CharField(max_length = 250)
    estado =  models.CharField(max_length = 250)
    def __str__(self):
        return f'{self.nombre}  {self.apellido} - {self.documento}'
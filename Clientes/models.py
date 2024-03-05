from django.db import models
from core.get_related_instances import get_related_instances
from django.db.models.deletion import ProtectedError


class Clientes(models.Model):
    class Meta: 
        verbose_name_plural = 'Clientes'
        
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
    def delete(self, using=None, keep_parents=False):
        # Comprueba si existen instancias activas de otros modelos que sean dependientes de esta instancia
        related_instances = get_related_instances(self)
        if related_instances:
            raise ProtectedError("Existen relaciones activas", related_instances)
        # Realiza el borrado lógico
        self.estado = 0
        self.save()
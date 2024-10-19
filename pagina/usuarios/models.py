from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

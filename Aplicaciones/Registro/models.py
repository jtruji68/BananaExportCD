from django.db import models

# Create your models here.


class Cargo(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

class Usuario(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

class Registro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    usuario = models.CharField(max_length=50)
    fecha_creacion = models.CharField(max_length=50)
    idlote = models.CharField(max_length=50)
    tipo_cosecha = models.CharField(max_length=50)
    id_vehiculo = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)

class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=6)
    conductor = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
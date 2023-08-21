from django.db import models

# Create your models here.
class libreria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class libro(models.Model):
    nombreLi = models.CharField(max_length=100)
    autorLi = models.CharField(max_length=200)
    categoriaLi = models.CharField(max_length=100)
    isbn = models.CharField(max_length=50)
    disponible = models.BooleanField(False)

class cliente(models.Model):
    id_Cli = models.IntegerField(max_length=10000)
    nombreCli = models.CharField(max_length=200)
    correoCli = models.EmailField(max_length=200)

    
from django.db import models

# Create your models here.
class libreria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

class libro(models.Model):
    nombreLi = models.CharField(max_length=100)
    autorLi = models.CharField(max_length=200)
    categoriaLi = models.CharField(max_length=100)
    isbn = models.CharField(primary_key=True, max_length=50)
    disponible = models.BooleanField(default=False)

    def __str__(self):
        return f"Nombre: {self.nombreLi} - ISBN: {self.isbn} "

class cliente(models.Model):
    numeroCli = models.AutoField(primary_key=True)
    nombreCli = models.CharField(max_length=200)
    correoCli = models.EmailField(max_length=200)

    def __str__(self):
        return f"ID: {self.numeroCli} - Nombre: {self.nombreCli}"

class trabajador(models.Model):
    id_trabj = models.AutoField(primary_key=True,default=0)
    nombreTrabj = models.CharField(max_length=200)
    telefonoTraj = models.CharField(max_length=10)
    corrreoTrabj = models.EmailField(max_length=200)

    def __str__(self):
        return f"ID: {self.id_trabj} - Nombre: {self.nombreTrabj}"

class disponible(models.Model):
    ISBN_libro = models.CharField(max_length=50)
    fecha_ini = models.DateField
    fecha_fin = models.DateField
    id_cli = models.IntegerField
    is_disponible = models.BooleanField(True)
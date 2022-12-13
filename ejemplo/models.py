from django.db import models

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"



class Mascota(models.Model):

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    raza = models.CharField(max_length=200)
    edad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.raza}, {self.edad}"


class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField()
    kilometros = models.IntegerField()

    def __str__(self):
      return f"{self.marca}, {self.modelo}, {self.ano}, {self.kilometros}"
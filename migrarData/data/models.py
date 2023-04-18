from django.db import models

# Create your models here.

class Padron(models.Model):
    CSala = models.CharField(max_length=5)
    sector = models.CharField(max_length=30)
    nombre_sala = models.CharField(max_length=30)
    entidad_municipal = models.CharField(max_length=30)
    TS_a_cargo = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.CSala} {self.sector} {self.nombre_sala} {self.entidad_municipal} {self.TS_a_cargo} "

class Fecha(models.Model):
    fecha = models.CharField(max_length=30)    

    def __str__(self):
        return f"{self.fecha}"

class Fecha_Padron(models.Model):
    CSala = models.ForeignKey( Padron, on_delete=models.CASCADE )
    Fecha = models.ForeignKey( Fecha, on_delete=models.CASCADE )
    valor = models.IntegerField()

    def __str__(self):
        return f"{self.CSala} {self.Fecha} {self.valor} "
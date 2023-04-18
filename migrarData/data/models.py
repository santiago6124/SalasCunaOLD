from django.db import models

# Create your models here.

import pandas as pd
import numpy
def migrar_data():
    df = pd.read_csv("..\migrarData\data\CONCILIACIÓN PADRONES 2023 - INGRESO DE PADRONES.csv")

    columns = [key for key in df]
    padron_columns = columns[0:6]
    fechas_columns = columns[6:len(columns)]

    for col in fechas_columns:
        filtt = Fecha.objects.filter(fecha = col)
        if len(list(filtt)) == 0:
            Fecha.objects.create(
                fecha = col
            )

    rango = len(df['C. DE SALA']) - 1
    for num in range(rango): # cambiar rango por un valor menor para testear

        filtt = Padron.objects.filter(CSala = df['C. DE SALA'][num])
        if len(list(filtt)) == 0:
            padron = Padron.objects.create(
                CSala = df['C. DE SALA'][num],
                sector = df['SECTOR'][num],
                nombre_sala = df['NOMBRE DE SALA'][num],
                entidad_municipal = df['ENTIDAD / MUNICIPALIDAD'][num],
                TS_a_cargo = df['TS A CARGO'][num],
            )

            for col in fechas_columns:
                valor = int(df[col][num]) if type(df[col][num]) == int else 0
                Fecha_Padron.objects.create(
                    padron_fk = padron,
                    fecha_fk = Fecha.objects.get(fecha = col),
                    valor = valor
                )

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
    padron_fk = models.ForeignKey( Padron, on_delete=models.CASCADE )
    fecha_fk = models.ForeignKey( Fecha, on_delete=models.CASCADE )
    valor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.padron_fk} {self.fecha_fk} {self.valor} "
    

migrar_data()

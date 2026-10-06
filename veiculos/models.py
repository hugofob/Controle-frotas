from django.db import models


class Veiculo(models.Model):
    placa = models.CharField(max_length=7)# charfield guardar texto
    ano = models.IntegerField()#integerfield guardar números
    cor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)

    def __str__(self):#Quando você precisar representar um veículo como texto, mostre a placa
        return self.placa

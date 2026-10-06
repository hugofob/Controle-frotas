from django.db import models


class Motorista(models.Model):

    nome = models.CharField(max_length=100)

    endereco = models.CharField(max_length=200)

    cnh = models.CharField(max_length=20)

    categoria = models.CharField(max_length=1)

    telefone = models.CharField(max_length=20)

    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome

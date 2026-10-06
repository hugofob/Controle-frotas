from django.db import models

class comentario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comentario = models.TextField()
    receber_info = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


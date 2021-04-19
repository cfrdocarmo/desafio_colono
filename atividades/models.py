from django.db import models
from datetime import datetime

from usuarios.models import Usuario


class Atividade(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default='')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=100)
    date_create = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo


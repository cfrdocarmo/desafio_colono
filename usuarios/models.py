from django.db import models
from datetime import datetime


class Usuario(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

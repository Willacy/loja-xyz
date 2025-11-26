from django.db import models

# Create your models here.
class Usuario (models.Model):
    nome = models.CharField()
    senha = models.CharField(
        max_length=48
    )
    def __str__ (self):
        return self.nome
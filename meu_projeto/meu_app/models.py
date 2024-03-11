from django.db import models
import os

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

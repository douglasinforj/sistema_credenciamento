from django.db import models
from django.contrib.auth.models import User

class Titular(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to="fotos/titulares", null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
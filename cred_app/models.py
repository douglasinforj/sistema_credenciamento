from django.db import models
from django.contrib.auth.models import User

class Titular(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to="fotos/titulares", null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Titular"
        verbose_name_plural = "Titulares"
 
    def __str__(self):
        return self.nome
    

class Convidado(models.Model):
    titular = models.ForeignKey(Titular, on_delete=models.CASCADE, related_name='convidados')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='fotos/convidados/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Convidado"
        verbose_name_plural = "Convidados"

    def __str__(self):
        return self.nome
    

class Evento(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome do Evento")
    data = models.DateTimeField(verbose_name="Data de Início")
    data_termino = models.DateTimeField(verbose_name="Data de Término", null=True, blank=True)
    local = models.CharField(max_length=255, verbose_name="Local do Evento")
    descricao = models.TextField(verbose_name="Descrição do Evento")
    foto = models.ImageField(upload_to='fotos/eventos/', null=True, blank=True, verbose_name="Foto do Evento")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nome

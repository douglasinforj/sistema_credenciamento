

from django.db import models
from django.contrib.auth.models import User

class Titular(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
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
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    foto = models.ImageField(upload_to='fotos/convidados/', null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # Novos campos para check-in e entrada dos convidados
    checkin_realizado = models.BooleanField(default=False, verbose_name="Check-in Realizado")
    entrada_confirmada = models.BooleanField(default=False, verbose_name="Entrada Confirmada")

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
    


#----------------Testar e subir para o github---------------------

class Participacao(models.Model):
    titular = models.ForeignKey('Titular', on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    convidados = models.ManyToManyField('Convidado', blank=True)
    data_inscricao = models.DateTimeField(auto_now_add=True)
    
    # Controle de participação do titular
    pagamento_confirmado = models.BooleanField(default=False, verbose_name="Pagamento Confirmado")
    data_pagamento = models.DateTimeField(null=True, blank=True, verbose_name="Data do Pagamento")
    checkin_realizado = models.BooleanField(default=False, verbose_name="Check-in Realizado")
    entrada_confirmada = models.BooleanField(default=False, verbose_name="Entrada Confirmada")

    class Meta:
        verbose_name = "Participação"
        verbose_name_plural = "Participações"

    def __str__(self):
        return f"{self.titular} em {self.evento}"

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para adicionar automaticamente os convidados 
        associados ao titular no momento da criação da participação.
        """
        super(Participacao, self).save(*args, **kwargs)
        
        # Adiciona os convidados do titular à participação automaticamente, se ainda não tiver convidados
        if not self.convidados.exists():
            convidados_titular = self.titular.convidados.all()  # Busca os convidados do titular
            self.convidados.add(*convidados_titular)  # Adiciona todos os convidados do titular

    def confirmar_entrada_convidado(self, convidado):
        """
        Método para confirmar a entrada de um convidado, garantindo que o titular já tenha feito check-in.
        """
        if not self.entrada_confirmada:
            raise ValueError(f"O titular {self.titular.nome} ainda não fez o check-in, então o convidado {convidado.nome} não pode acessar.")
        
        convidado.checkin_realizado = True
        convidado.save()
        return f"Entrada confirmada para o convidado {convidado.nome}."
    









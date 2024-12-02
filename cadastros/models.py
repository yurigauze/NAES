from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import datetime
from django.conf import settings


# Create your models here.

class Cidade(models.Model):
    name = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}/{self.estado}"

    class Meta:
        ordering = ["name", "estado"]

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    nascimento = models.DateField(default=datetime.date(2000, 1, 1), verbose_name="data de nascimento")
    email = models.EmailField(max_length=120, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_completo}"
    
    class Meta:
        ordering = ["nome_completo"]

class Prefeitura(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome}"

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    undMedida = models.CharField(max_length=3)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class OrdemDeCompra(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    prefeitura = models.ForeignKey(Prefeitura, on_delete=models.PROTECT)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT, null=False)
    entregue = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class ItemOrdemDeCompra(models.Model):
    ordem_de_compra = models.ForeignKey(OrdemDeCompra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
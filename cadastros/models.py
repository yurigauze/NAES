from django.db import models
from django.db.models import Sum
import datetime

# Create your models here.
class Cidade(models.Model):
    name = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return f"{self.name}/{self.estado}"
    
    class Meta:
        ordering = ["name", "estado"]
    
    
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=150)
    nascimento = models.DateField(default=datetime.date(
        2000, 1, 1), verbose_name="data de nascimento")
    email = models.EmailField(max_length=120, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome_completo}"
    
class Prefeitura(models.Model):
    nome = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nome}"
    
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    undMedida = models.CharField(max_length=3)

    
class OrdemDeCompra(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    prefeitura = models.ForeignKey(
        Prefeitura, on_delete=models.PROTECT)
    cidade = models.ForeignKey(
        Cidade, on_delete=models.PROTECT, null=False)
    entregue = models.BooleanField(default=False)
    

class ItemOrdemDeCompra(models.Model):
    ordem_de_compra = models.ForeignKey(
        OrdemDeCompra, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
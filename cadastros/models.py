from django.db import models

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
    nascimento = models.DateField(verbose_name="data de nascimento")
    cpf = models.CharField(max_length=14, verbose_name="CPF", unique=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    rede_social = models.URLField(max_length=255, blank=True,
        null=True, help_text="Informe o link do Instagram, Facebook, LinkedIn ou outra rede social.")
    salario = models.DecimalField(verbose_name="salário",
        decimal_places=2, max_digits=9)
    
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
    
    
class OrdemDeCompra(models.Model):
    data = models.DateTimeField(auto_now_add=True)
import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SOE.settings")
django.setup()

from cadastros.models import Prefeitura, Cidade, Pessoa, Produto
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def populate():

    user = get_user_model().objects.get(username='admin')

    # Inserir cidades fictícias
    cidade1 = Cidade.objects.create(
        name='São Paulo',
        estado='SP',
        user=user
    )
    
    cidade2 = Cidade.objects.create(
        name='Rio de Janeiro',
        estado='RJ',
        user=user
    )
    cidade3 = Cidade.objects.create(
        name='Belo Horizonte',
        estado='MG',
        user=user
    )
    cidade4 = Cidade.objects.create(
        name='Maringa',
        estado='PR',
        user=user
    )
    cidade5 = Cidade.objects.create(
        name='Tamboara',
        estado='PR',
        user=user
    )
    cidade6 = Cidade.objects.create(
        name='Alto Paraná',
        estado='PR',
        user=user
    )

    # Inserir prefeituras fictícias
    prefeitura1 = Prefeitura.objects.create(
        nome='Prefeitura de São Paulo',
        cidade=cidade1,
        cnpj='12.345.678/0001-90',
        cadastrado_em=datetime.now(),
        atualizado_em=datetime.now(),
        user=user
    )

    prefeitura2 = Prefeitura.objects.create(
        nome='Prefeitura do Rio de Janeiro',
        cidade=cidade2,
        cnpj='98.765.432/0001-12',
        cadastrado_em=datetime.now(),
        atualizado_em=datetime.now(),
        user=user
    )

    prefeitura3 = Prefeitura.objects.create(
        nome='Prefeitura de Belo Horizonte',
        cidade=cidade3,
        cnpj='34.567.890/0001-23',
        cadastrado_em=datetime.now(),
        atualizado_em=datetime.now(),
        user=user
    )
    prefeitura4 = Prefeitura.objects.create(
        nome='Prefeitura de Tamboara',
        cidade=cidade3,
        cnpj='34.567.890/0001-23',
        cadastrado_em=datetime.now(),
        atualizado_em=datetime.now(),
        user=user
    )
    prefeitura5 = Prefeitura.objects.create(
        nome='Prefeitura de Alto Paraná',
        cidade=cidade3,
        cnpj='34.567.890/0001-23',
        cadastrado_em=datetime.now(),
        atualizado_em=datetime.now(),
        user=user
    )

    # Inserir pessoas fictícias
    pessoa1 = Pessoa.objects.create(
        nome_completo="João Silva",
        nascimento=datetime(1990, 5, 15),
        email="joao.silva@email.com",
        cargo="Analista de Sistemas",
        cidade=cidade1,
        user=user
    )
    
    pessoa2 = Pessoa.objects.create(
        nome_completo="Maria Oliveira",
        nascimento=datetime(1985, 8, 25),
        email="maria.oliveira@email.com",
        cargo="Desenvolvedora",
        cidade=cidade2,
        user=user
    )
    
    pessoa3 = Pessoa.objects.create(
        nome_completo="Carlos Souza",
        nascimento=datetime(1992, 3, 30),
        email="carlos.souza@email.com",
        cargo="Gerente de Projetos",
        cidade=cidade3,
        user=user
    )

    # Inserir produtos fictícios
    produto1 = Produto.objects.create(
        nome="Cadeira de Escritório",
        undMedida="UN",
        user=user
    )

    produto2 = Produto.objects.create(
        nome="Mesa de Reunião",
        undMedida="UN",
        user=user
    )

    produto3 = Produto.objects.create(
        nome="Computador Desktop",
        undMedida="UN",
        user=user
    )
    produto4 = Produto.objects.create(
        nome="Mouse",
        undMedida="UN",
        user=user
    )

    produto35= Produto.objects.create(
        nome="Teclado",
        undMedida="UN",
        user=user
    )


    print('Dados inseridos com sucesso!')

if __name__ == '__main__':
    populate()

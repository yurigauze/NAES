from django_filters import FilterSet
from .models import Cidade, Pessoa, Prefeitura


class CidadeFilter(FilterSet):
    class Meta:
        model = Cidade
        fields = {'name' : ['icontains'], 'estado': ['icontains']}


class PessoaFilter(FilterSet):
    class Meta:
        model = Pessoa
        fields = {'nome_completo': ['icontains'], 'email' : ['icontains']}



class PrefeituraFilter(FilterSet):
    class Meta:
        model = Prefeitura
        fields = {'nome' : ['icontains'], 'cnpj': ['icontains']}

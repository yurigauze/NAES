import django_filters
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



class PrefeituraFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='icontains')
    cidade = django_filters.CharFilter(
        field_name='cidade__nome', lookup_expr='icontains')  
    user = django_filters.CharFilter(
        field_name='user__username', lookup_expr='icontains')

    class Meta:
        model = Prefeitura
        fields = {'nome', 'cidade', 'user'}

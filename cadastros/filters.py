from django_filters import FilterSet
from .models import Cidade


class CidadeFilter(FilterSet):
    class Meta:
        model = Cidade
        fields = {'name' : ['icontains'], 'estado': ['icontains']}
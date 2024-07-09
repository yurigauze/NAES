from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from cadastros.models import Cidade
from cadastros.models import Pessoa

# Create your views here.
class CidadeCreat(CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
class CidadeUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    model = Cidade
    fields = ['name']
    
class PessoaCreat(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'data_nascimento', 'cpf', 'email', 'rede_social', 'salario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'data_nascimento', 'email', 'rede_social', 'salario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

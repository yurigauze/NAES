from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ListView

from cadastros.models import Cidade
from cadastros.models import Pessoa

# Create your views here.
class CidadeCreat(CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')
    
    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados
    
class CidadeUpdate(UpdateView):
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    fields = ['name']
    
    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados
    
class CidadeDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidade')
    model = Cidade
    
class CidadeList(ListView):
    template_name = 'cadastros/list/cidade.html'
    model = Cidade
    
    
    
class PessoaCreat(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'data_nascimento', 'cpf', 'email', 'rede_social', 'salario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'data_nascimento', 'email', 'rede_social', 'salario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
        
    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados


class PessoaDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    model = Pessoa


class PessoaList(ListView):
    template_name = ''
    model = Pessoa

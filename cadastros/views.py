from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from cadastros.models import Cidade
from cadastros.models import Pessoa
from cadastros.models import Prefeitura
from cadastros.models import Produto
from cadastros.models import OrdemDeCompra
from cadastros.models import ItemOrdemDeCompra


# Create your views here.
class CidadeCreate(CreateView):
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
    
    
    
class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo']
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
    

class PrefeituraCreate(CreateView):
    model = Prefeitura
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Prefeitura'
        return dados


class PrefeituraUpdate(UpdateView):
    model = Prefeitura
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class PrefeituraDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    model = Prefeitura


class PrefeituraList(ListView):
    template_name = ''
    model = Prefeitura
    
    
class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar novo Produto'
        return dados


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class ProdutoDelete(DeleteView):
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('index')
    model = Produto
    
class ProdutoList(ListView):
    template_name = ''
    model = Produto
    


class OrdemDeCompraDetail(ListView):
    model = OrdemDeCompra
    template_name = 'ordem_de_compra_detail.html'
    
    
class OrdemDeCompraCreate(CreateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Ordem de Compra'
        return dados


class OrdemDeCompraUpdate(UpdateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class OrdemDeCompraDelete(DeleteView):
    model = OrdemDeCompra
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')

class OrdemDeCompraList(ListView):
    model = OrdemDeCompra
    template_name = 'cadastros/form-excluir.html'
    context_object_name = 'ordens_de_compra'    
    
    

class ItemOrdemDeCompraCreate(CreateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'item_ordem_de_compra_form.html'

    def form_valid(self, form):
        ordem_de_compra = get_object_or_404(
            OrdemDeCompra, pk=self.kwargs['pk'])
        form.instance.ordem_de_compra = ordem_de_compra
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.kwargs['pk']})


class ItemOrdemDeCompraUpdate(UpdateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'item_ordem_de_compra_form.html'

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.object.ordem_de_compra.pk})

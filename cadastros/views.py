from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from cadastros.models import Cidade, Pessoa, Prefeitura, Produto, OrdemDeCompra, ItemOrdemDeCompra


class CidadeCreate(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados


class CidadeUpdate(LoginRequiredMixin, UpdateView):
    model = Cidade
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadeDelete(GroupRequiredMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador"]


class CidadeList(LoginRequiredMixin, ListView):
    model = Cidade
    template_name = 'cadastros/list/cidade.html'


class PessoaCreate(LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados


class PessoaDelete(GroupRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador"]


class PessoaList(LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'cadastros/list/pessoa.html'


class PrefeituraCreate(LoginRequiredMixin, CreateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Prefeitura'
        return dados


class PrefeituraUpdate(LoginRequiredMixin, UpdateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class PrefeituraDelete(GroupRequiredMixin, DeleteView):
    model = Prefeitura
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required =["Administrador"]


class PrefeituraList(LoginRequiredMixin, ListView):
    model = Prefeitura
    template_name = 'cadastros/list/prefeitura.html'


class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar novo Produto'
        return dados


class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class ProdutoDelete(GroupRequiredMixin, DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador"]


class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'cadastros/list/produto.html'


class OrdemDeCompraDetail(LoginRequiredMixin, DetailView):
    model = OrdemDeCompra
    template_name = 'cadastros/ordem_de_compra_detail.html'
    context_object_name = 'ordem_de_compra'


class OrdemDeCompraCreate(LoginRequiredMixin, CreateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Ordem de Compra'
        return dados


class OrdemDeCompraUpdate(LoginRequiredMixin, UpdateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de Ordem de Compra #{self.object.pk}"
        return dados


class OrdemDeCompraDelete(GroupRequiredMixin, DeleteView):
    model = OrdemDeCompra
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-ordens-de-compra')
    group_required = ["Administrador"]


class OrdemDeCompraList(LoginRequiredMixin, ListView):
    model = OrdemDeCompra
    template_name = 'cadastros/list/ordem_de_compra.html'
    context_object_name = 'ordens_de_compra'


class ItemOrdemDeCompraCreate(LoginRequiredMixin, CreateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'cadastros/item_ordem_de_compra_form.html'

    def form_valid(self, form):
        ordem_de_compra = get_object_or_404(
            OrdemDeCompra, pk=self.kwargs['pk'])
        form.instance.ordem_de_compra = ordem_de_compra
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.kwargs['pk']})


class ItemOrdemDeCompraUpdate(LoginRequiredMixin, UpdateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'cadastros/item_ordem_de_compra_form.html'

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.object.ordem_de_compra.pk})


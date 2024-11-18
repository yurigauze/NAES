from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from usuarios.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from cadastros.models import Cidade, Pessoa, Prefeitura, Produto, OrdemDeCompra, ItemOrdemDeCompra

from django.contrib.messages.views import SuccessMessageMixin




# Cidade
class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin,CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador", "Editor"]
    sucess_message = "Cidade %(nome)s Adicionada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Define o usuário atual como o proprietário
        return super().form_valid(form)

class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class CidadeList(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Cidade
    template_name = 'cadastros/list/cidade.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Pessoa
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador", "Editor"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Pessoa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Pessoa
    template_name = 'cadastros/list/pessoa.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Prefeitura
class PrefeituraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador", "Editor"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PrefeituraUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class PrefeituraDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Prefeitura
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class PrefeituraList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Prefeitura
    template_name = 'cadastros/list/prefeitura.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Produto
class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador", "Editor"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'cadastros/list/produto.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Ordem de Compra
class OrdemDeCompraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')
    group_required = ["Administrador", "Editor"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrdemDeCompraUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class OrdemDeCompraDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = OrdemDeCompra
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-ordens-de-compra')
    group_required = ["Administrador"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class OrdemDeCompraList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = OrdemDeCompra
    template_name = 'cadastros/list/ordem_de_compra.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


# Item da Ordem de Compra
class ItemOrdemDeCompraCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'cadastros/item_ordem_de_compra_form.html'
    group_required = ["Administrador", "Editor"]

    def form_valid(self, form):
        ordem_de_compra = get_object_or_404(OrdemDeCompra, pk=self.kwargs['pk'], user=self.request.user)
        form.instance.ordem_de_compra = ordem_de_compra
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.kwargs['pk']})

class ItemOrdemDeCompraUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'cadastros/item_ordem_de_compra_form.html'
    group_required = ["Administrador", "Editor"]

    def get_queryset(self):
        return super().get_queryset().filter(ordem_de_compra__user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.object.ordem_de_compra.pk})



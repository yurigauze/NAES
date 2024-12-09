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

from django_filters.views import FilterView
from .filters import CidadeFilter, PessoaFilter, PrefeituraFilter



# Cidade
class CidadeCreate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador", "Editor"]
    success_message = "Cidade %(name)s Adicionada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user

        if Cidade.objects.filter(name=form.instance.name, estado=form.instance.estado, user=self.request.user).exists():
            form.add_error('name', 'Você já cadastrou essa cidade.')
            return self.form_invalid(form)

        return super().form_valid(form)


class CidadeUpdate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador", "Editor"]
    success_message = "Cidade %(name)s atualizada!"

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user and not self.request.user.groups.filter(name="Administrador").exists():
            return redirect('listar-cidades')
        return super().form_valid(form)


class CidadeDelete(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')
    group_required = ["Administrador"]
    success_message = "Cidade excluída!"

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


class CidadeList(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, FilterView):
    model = Cidade
    template_name = 'cadastros/list/cidade.html'
    group_required = ["Administrador", "Editor"]
    paginate_by = 50
    filterset_class = CidadeFilter

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user) 


# Pessoa
class PessoaCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador", "Editor"]
    success_message = "Pessoa %(nome_completo)s cadastrada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        if Pessoa.objects.filter(email=form.instance.email, user=self.request.user).exists():
            form.add_error('email', 'Já existe uma pessoa cadastrada com esse email.')
            return self.form_invalid(form)
        
        return super().form_valid(form)


class PessoaUpdate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador", "Editor"]
    success_message = "Pessoa %(nome_completo)s atualizada!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user and not self.request.user.groups.filter(name="Administrador").exists():
            return redirect('listar-pessoas')
        return super().form_valid(form)


class PessoaDelete(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Pessoa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoas')
    group_required = ["Administrador"]
    success_message = "Pessoa excluída!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


class PessoaList(GroupRequiredMixin, LoginRequiredMixin, ListView,SuccessMessageMixin, FilterView):
    model = Pessoa
    template_name = 'cadastros/list/pessoa.html'
    group_required = ["Administrador", "Editor"]
    paginate_by = 50
    filterset_class = PessoaFilter

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


# Prefeitura
class PrefeituraCreate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Prefeitura
    fields = ['nome', 'cnpj', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador", "Editor"]
    success_message = "Prefeitura %(nome)s cadastrada com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user

        if Prefeitura.objects.filter(nome=form.instance.nome, cidade=form.instance.cidade, user=self.request.user).exists():
            form.add_error(
                'nome', 'Já existe uma prefeitura cadastrada nessa cidade.')
            return self.form_invalid(form)

        return super().form_valid(form)


class PrefeituraUpdate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Prefeitura
    fields = ['nome', 'cnpj', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador", "Editor"]
    success_message = "Prefeitura %(nome)s atualizada!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user and not self.request.user.groups.filter(name="Administrador").exists():
            return redirect('listar-prefeituras')
        return super().form_valid(form)


class PrefeituraDelete(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Prefeitura
    template_name = 'cadastros/form-excluir.html'
    context_object_name = 'object'
    success_url = reverse_lazy('listar-prefeituras')
    group_required = ["Administrador"]
    success_message = "Prefeitura excluída!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)

    

class PrefeituraList(GroupRequiredMixin, LoginRequiredMixin, ListView, SuccessMessageMixin, FilterView):
    model = Prefeitura
    template_name = 'cadastros/list/prefeitura.html'
    group_required = ["Administrador", "Editor"]
    paginate_by = 50
    filterset_class = PrefeituraFilter
    

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)


# Produto
class ProdutoCreate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador", "Editor"]
    success_message = "Produto %(nome)s cadastrado com sucesso!"

    def form_valid(self, form):
        form.instance.user = self.request.user

        if Produto.objects.filter(nome=form.instance.nome, user=self.request.user).exists():
            form.add_error(
                'nome', 'Já existe um produto cadastrado com esse nome.')
            return self.form_invalid(form)

        return super().form_valid(form)


class ProdutoUpdate(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador", "Editor"]
    success_message = "Produto %(nome)s atualizada!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        if form.instance.user != self.request.user and not self.request.user.groups.filter(name="Administrador").exists():
            return redirect('listar-produtos')
        return super().form_valid(form)


class ProdutoDelete(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')
    group_required = ["Administrador"]
    success_message = "Produto excluída!"


    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
        return super().get_queryset().filter(user=self.request.user)



class ProdutoList(GroupRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Produto
    template_name = 'cadastros/list/produto.html'
    group_required = ["Administrador", "Editor"]
    paginate_by = 50
    

    def get_queryset(self):
        if self.request.user.groups.filter(name="Administrador").exists():
            return super().get_queryset()
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
    paginate_by = 50

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



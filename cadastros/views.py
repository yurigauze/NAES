from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from cadastros.models import Cidade, Pessoa, Prefeitura, Produto, OrdemDeCompra, ItemOrdemDeCompra


class CidadeCreate(CreateView):
    model = Cidade
    fields = ['name', 'estado']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar cidade'
        return dados


class CidadeUpdate(UpdateView):
    model = Cidade
    fields = ['name']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cidades')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Editar registro de Cidade'
        return dados


class CidadeDelete(DeleteView):
    model = Cidade
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cidades')


class CidadeList(ListView):
    model = Cidade
    template_name = 'cadastros/list/cidade.html'


class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoas')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Pessoa'
        return dados


class PessoaUpdate(UpdateView):
    model = Pessoa
    fields = ['nome_completo', 'nascimento', 'email', 'cargo', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pessoa')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome_completo}"
        return dados


class PessoaDelete(DeleteView):
    model = Pessoa
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pessoas')


class PessoaList(ListView):
    model = Pessoa
    template_name = 'cadastros/list/pessoa.html'


class PrefeituraCreate(CreateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Prefeitura'
        return dados


class PrefeituraUpdate(UpdateView):
    model = Prefeitura
    fields = ['nome', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-prefeituras')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class PrefeituraDelete(DeleteView):
    model = Prefeitura
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-prefeituras')


class PrefeituraList(ListView):
    model = Prefeitura
    template_name = 'cadastros/list/prefeitura.html'


class ProdutoCreate(CreateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar novo Produto'
        return dados


class ProdutoUpdate(UpdateView):
    model = Produto
    fields = ['nome', 'undMedida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produtos')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de {self.object.nome}"
        return dados


class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produtos')


class ProdutoList(ListView):
    model = Produto
    template_name = 'cadastros/list/produto.html'


class OrdemDeCompraDetail(DetailView):
    model = OrdemDeCompra
    template_name = 'cadastros/ordem_de_compra_detail.html'
    context_object_name = 'ordem_de_compra'


class OrdemDeCompraCreate(CreateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = 'Cadastrar nova Ordem de Compra'
        return dados


class OrdemDeCompraUpdate(UpdateView):
    model = OrdemDeCompra
    fields = ['prefeitura', 'cidade', 'produtos', 'entregue']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ordens-de-compra')

    def get_context_data(self, **kwargs):
        dados = super().get_context_data(**kwargs)
        dados['titulo'] = f"Editar registro de Ordem de Compra #{self.object.pk}"
        return dados


class OrdemDeCompraDelete(DeleteView):
    model = OrdemDeCompra
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-ordens-de-compra')


class OrdemDeCompraList(ListView):
    model = OrdemDeCompra
    template_name = 'cadastros/list/ordem_de_compra.html'
    context_object_name = 'ordens_de_compra'


class ItemOrdemDeCompraCreate(CreateView):
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


class ItemOrdemDeCompraUpdate(UpdateView):
    model = ItemOrdemDeCompra
    fields = ['produto', 'valor']
    template_name = 'cadastros/item_ordem_de_compra_form.html'

    def get_success_url(self):
        return reverse_lazy('ordem-detail', kwargs={'pk': self.object.ordem_de_compra.pk})


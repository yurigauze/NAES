from django.urls import path

from .views import CidadeCreate, CidadeUpdate, CidadeDelete, CidadeList
from .views import PessoaCreate, PessoaUpdate, PessoaDelete, PessoaList
from .views import OrdemDeCompraCreate, OrdemDeCompraUpdate, OrdemDeCompraDelete, OrdemDeCompraList
from .views import ProdutoCreate, ProdutoUpdate, ProdutoDelete, ProdutoList
from .views import PrefeituraCreate, PrefeituraUpdate, PrefeituraDelete, PrefeituraList

urlpatterns = [
    path('cadastrar/cidade/',CidadeCreate.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidades/', CidadeList.as_view(), name='listar-cidades'),
    
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('listar/pessoas/', PessoaList.as_view(), name='listar-pessoas'),
    
    path('cadastrar/prefeitura/', PrefeituraCreate.as_view(),
         name='cadastrar-prefeitura'),
    path('editar/prefeitura/<int:pk>/',
         PrefeituraUpdate.as_view(), name='editar-prefeitura'),
    path('excluir/prefeitura/<int:pk>/',
         PrefeituraDelete.as_view(), name='excluir-prefeitura'),
    path('listar/prefeituras/', PrefeituraList.as_view(),
         name='listar-prefeituras'),
    
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('editar/produto/<int:pk>/',
         ProdutoUpdate.as_view(), name='editar-produto'),
    path('excluir/produto/<int:pk>/',
         ProdutoDelete.as_view(), name='excluir-produto'),
    path('listar/produtos/', ProdutoList.as_view(), name='listar-produtos'),
    
    path('cadastrar/ordem-de-compra/', OrdemDeCompraCreate.as_view(),
         name='cadastrar-ordem-de-compra'),
    path('editar/ordem-de-compra/<int:pk>/',
         OrdemDeCompraUpdate.as_view(), name='editar-ordem-de-compra'),
    path('excluir/ordem-de-compra/<int:pk>/',
         OrdemDeCompraDelete.as_view(), name='excluir-ordem-de-compra'),
    path('listar/ordens-de-compra/', OrdemDeCompraList.as_view(),
         name='listar-ordens-de-compra'),

]

from django.urls import path

from .views import CidadeCreat, CidadeUpdate, CidadeDelete, CidadeList
from .views import PessoaCreat, PessoaUpdate, PessoaDelete, PessoaList

urlpatterns = [
    path('cadastrar/cidade/',CidadeCreat.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('excluir/cidade/<int:pk>/', CidadeDelete.as_view(), name='excluir-cidade'),
    path('listar/cidades/', CidadeList.as_view(), name='listar-cidades'),
    
    path('cadastrar/pessoa/', PessoaCreat.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
    path('excluir/pessoa/<int:pk>/', PessoaDelete.as_view(), name='excluir-pessoa'),
    path('listar/pessoas/', PessoaList.as_view(), name='listar-pessoas'),

]

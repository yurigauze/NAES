from django.urls import path

from .views import CidadeCreat, CidadeUpdate
from .views import PessoaCreat, PessoaUpdate

urlpatterns = [
    path('cadastrar/cidade/',CidadeCreat.as_view(), name='cadastrar-cidade'),
    path('editar/cidade/<int:pk>/', CidadeUpdate.as_view(), name='editar-cidade'),
    path('cadastrar/pessoa/', PessoaCreat.as_view(), name='cadastrar-pessoa'),
    path('editar/pessoa/<int:pk>/', PessoaUpdate.as_view(), name='editar-pessoa'),
]

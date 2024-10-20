from django.urls import path
from django.contrib.auth import views
from django.urls import reverse_lazy
from .views import RegisterView, UserListView

urlpatterns = [
    # Crie suas urls para as views
    path("entrar/", views.LoginView.as_view(
            template_name="usuarios/form.html",
            extra_context={
                'titulo': 'Autenticação de usuários'
            }
        ), name="login"),
    
    path("sair/", views.LogoutView.as_view(
        next_page=reverse_lazy('index')
    ), name="logout"),
    
    path("minha-senha/", views.PasswordChangeView.as_view(
            template_name="cadastros/form.html",
            success_url=reverse_lazy("index"),
            extra_context={
                'titulo': 'Atualizar minha senha'
            }
        ), name="alterar-senha"),
    
    # Adicione a URL para o registro de usuários
    path('cadastrar/', RegisterView.as_view(), name='cadastrar_usuario'),
    path('usuarios/', UserListView.as_view(), name='user_list'),
]

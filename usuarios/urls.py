from django.urls import path
from django.contrib.auth import views
from django.urls import reverse_lazy

urlpatterns = [
    # Crie suas urls para as views
    # path("entrar/", views.LoginView.as_view(), name="login"),
    
    path("entrar/", views.LoginView.as_view(
            template_name="usuarios/form.html",
            extra_context={
                'titulo' : 'Autenticação de usuários'
            }
        ), name="login"),
    
    path("sair/", views.LogoutView.as_view(), name="logout"),
    
    path("minha-senha/", views.PasswordChangeView.as_view(
            template_name="cadastros/form.html",
            success_url = reverse_lazy("index"),
            extra_context={
                'titulo': 'Atualizar minha senha'
            }
        ), name="alterar-senha"),
]
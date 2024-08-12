from django.urls import path, reverse_lazy
from django.contrib.auth import views


urlpatterns = [
    # path("entrar/", views.LoginView.as_view(template_name=""), name="login"),
    path('login/', views.LoginView.as_view(
        template_name='cadastros/form.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),
    
    path("sair/", views.LogoutView.as_view(), name='logout'),
    
    path('senha/', views.PasswordChangeView.as_view(
        template_name='cadastros/form.html',
        extra_context={'titulo': 'Alterar senha atual'},
        success_url=reverse_lazy('index')
    ), name="alterar-senha"),
]

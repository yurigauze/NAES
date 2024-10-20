from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from usuarios.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin


class RegisterView(GroupRequiredMixin, LoginRequiredMixin, View):
    group_required = ["Administrador"]

    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'usuarios/form.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True  # Define que o novo usuário é um membro da equipe
            user.is_active = True  # Certifique-se de que o usuário está ativo
            user.save()
            return redirect('login')
        else:
            print(form.errors)
        return render(request, 'usuarios/form.html', {'form': form})


class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'usuarios/user_list.html'  # Crie esse template
    context_object_name = 'users'

    def get_queryset(self):
        return CustomUser.objects.all()  # Aqui você pode filtrar se necessário
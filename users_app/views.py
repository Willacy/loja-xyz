from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def deslogar (request):
    """Faz o logout do usuario e redireciona para  a pagina inicial"""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def registrar(request):
    """Registra um novo usuário"""
    if request.method != 'POST':
        # Exibe um formulario em branco
        form = UserCreationForm()
    else:
        # Processa o formulario preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'registrar.html', context)  


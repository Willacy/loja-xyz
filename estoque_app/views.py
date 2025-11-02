from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Categoria
from .forms import CategoriaForm

# Página inicial
def index(request):
    """Pagina inicial do sistema """
    return render(request, 'index.html')



# >>>>>>>>>> CATEGORIA <<<<<<<<<<
@login_required
def categorias(request):
    """Mostra as categorias cadastradas"""
    categorias = Categoria.objects.all().order_by('nome')
    contexto = {'categorias': categorias}
    return render(request, 'categoria/categorias.html', contexto)

# Função para adicionar uma nova categoria
@login_required
def nova_categoria(request):
    """ Adiciona uma nova categoria"""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('categorias'))
    else:
        form = CategoriaForm()
    contexto = {'form': form}
    return render(request, 'categoria/nova_categoria.html', contexto)
        

# Função para editar categoria
@login_required
def editar_categoria(request, categoria_id):
    """Edita uma categoria existente"""
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(data=request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('categorias'))
    else:
        form = CategoriaForm(instance=categoria)    
    contexto = {'form': form, 'categoria': categoria}
    return render(request, 'categoria/editar_categoria.html', contexto)

# Função para deletar categoria
@login_required
def excluir_categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return HttpResponseRedirect(reverse('categorias'))
    contexto = {'categoria': categoria}
    return render(request, 'categoria/excluir_categoria.html', contexto)

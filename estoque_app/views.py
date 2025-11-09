from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Categoria, Fornecedor, Produto
from .forms import CategoriaForm, FornecedorForm, ProdutoForm

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



# >>>>>>>>>> FORNECEDORES <<<<<<<<<<
# Função para listar os fornecedores
@login_required
def fornecedores(request):
    """Mostra todos os fornecedores cadastrado"""
    fornecedores = Fornecedor.objects.all().order_by('nome')
    contexto = {'fornecedores' : fornecedores}
    return render(request,'fornecedor/fornecedores.html', contexto)

# Função para adicionar uma novo fornecedor
@login_required
def novo_fornecedor(request):
    """ Adiciona um novo fornecedor"""
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('fornecedores'))
    else:
        form = FornecedorForm()
    contexto = {'form': form}
    return render(request, 'fornecedor/novo_fornecedor.html', contexto)

# Função para editar forcedor
@login_required
def editar_fornecedor(request, fornecedor_id):
    """Edita um fornecedor existente"""
    fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    if request.method == 'POST':
        form = FornecedorForm(data=request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fornecedores'))
    else:
        form = FornecedorForm(instance=fornecedor)    
    contexto = {'form': form, 'fornecedor': fornecedor}
    return render(request, 'fornecedor/editar_fornecedor.html', contexto)

# Função para deletar fornecedor
@login_required
def excluir_fornecedor(request, fornecedor_id):
    fornecedor = Fornecedor.objects.get(id=fornecedor_id)
    if request.method == 'POST':
        fornecedor.delete()
        return HttpResponseRedirect(reverse('fornecedores'))
    contexto = {'fornecedor': fornecedor}
    return render(request, 'fornecedor/excluir_fornecedor.html', contexto)

# >>>>>>>>>> PRODUTOS <<<<<<<<<<
# Função para listar os Produtos
@login_required
def produtos(request):
    """Mostra todos os produtos cadastrado"""
    produtos = Produto.objects.all().order_by('nome')
    contexto = {'produtos' : produtos}
    return render(request,'produto/produtos.html', contexto)

# Função para adicionar uma novo Produto
@login_required
def novo_produto(request):
    """ Adiciona um novo produto"""
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('produtos'))
    else:
        form = ProdutoForm()
    contexto = {'form': form}
    return render(request, 'produto/novo_produto.html', contexto)

# Função para editar Produto
@login_required
def editar_produto(request, produto_id):
    """Edita um produto existente"""
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(data=request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produtos'))
    else:
        form = ProdutoForm(instance=produto)    
    contexto = {'form': form, 'produto': produto}
    return render(request, 'produto/editar_produto.html', contexto)

# Função para deletar produto
@login_required
def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        produto.delete()
        return HttpResponseRedirect(reverse('produtos'))
    contexto = {'produto': produto}
    return render(request, 'produto/excluir_produto.html', contexto)

"""
URL configuration for lojaxyz_projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # >>>>>>>>>> REFERENTE A CATEGORIA <<<<<<<<<<
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/nova', views.nova_categoria, name='nova_categoria'),
    path('categoria/<categoria_id>/editar', views.editar_categoria, name='editar_categoria'),
    path('categoria/<categoria_id>/deletar/', views.excluir_categoria, name='excluir_categoria'),
    
    # >>>>>>>>>> REFERENTE A FORNECEDOR <<<<<<<<<<
    path('fornecedores', views.fornecedores, name='fornecedores'),
    path('fornecedor/novo', views.novo_fornecedor, name='novo_fornecedor'),
    path('fornecedor/<fornecedor_id>/editar', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedor/<fornecedor_id>/deletar/', views.excluir_fornecedor, name='excluir_fornecedor'),
    
    # >>>>>>>>>> REFERENTE A PRODUTO <<<<<<<<<<
    path('produtos', views.produtos, name='produtos'),
    path('produto/novo', views.novo_produto, name='novo_produto'),
    path('produto/<produto_id>/editar', views.editar_produto, name='editar_produto'),
    path('produto/<produto_id>/deletar/', views.excluir_produto, name='excluir_produto'),
]
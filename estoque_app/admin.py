from django.contrib import admin
from .models import Categoria, Produto, Fornecedor, EntradaProduto, Mov_entrada, SaidaProduto, Mov_saida

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(EntradaProduto)
admin.site.register(Mov_entrada)
admin.site.register(SaidaProduto)
admin.site.register(Mov_saida)

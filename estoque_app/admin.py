from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Fornecedor)
admin.site.register(EntradaProduto)
admin.site.register(SaidaProduto)
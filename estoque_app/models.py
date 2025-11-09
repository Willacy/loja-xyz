from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    quantidade_estoque = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')

    def __str__(self):
        return self.nome
    
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    
class EntradaProduto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, related_name='entradas')
    quantidade = models.IntegerField()
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Entrada de {self.quantidade} unidades de...'
    
class Mov_entrada(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='mov_entradas')
    entrada_produto = models.ForeignKey(EntradaProduto, on_delete=models.CASCADE, related_name='mov_entradas')

    def __str__(self):
        return f'Movimento de entrada: {self.entrada_produto.quantidade} unidades de {self.produto.nome}'

class SaidaProduto(models.Model):
    quantidade = models.IntegerField()
    data_saida = models.DateTimeField(auto_now_add=True)
    motivo = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Saída de {self.quantidade} unidades de...'
    
class Mov_saida(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='mov_saidas')
    saida_produto = models.ForeignKey(SaidaProduto, on_delete=models.CASCADE, related_name='mov_saidas')

    def __str__(self):
        return f'Movimento de saída: {self.saida_produto.quantidade} unidades de {self.produto.nome}'

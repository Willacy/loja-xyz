from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User
from .models import *

# form da Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        labels = {'nome': '', 'descricao': ''}
        widgets = {'descricao': forms.Textarea(attrs={'cols': 80})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
                {
                    'placeholder':'Nome',
                    'class':'col form-control my-2 p-2'
                }
            )
        self.fields['descricao'].widget.attrs.update(
                {
                    'placeholder':'Descrição',
                    'class':'col form-control my-2 p-2'
                }
            )

# form do fornecedor    
class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = [
            'nome', 
            'cnpj', 
            'email',
            'telefone'
            ]
        labels = {
            'nome':'Nome',
            'cnpj':'C.N.P.J.',
            'email':'E-mail',
            'telefone':'Telefone'
            }

# form do Produto    
class ProdutoForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all().order_by('nome'), empty_label='Selecione uma categoria')
    class Meta:
        model = Produto
        fields = [
            'categoria',
            'nome', 
            'descricao', 
            'quantidade_estoque'
            ]
        labels = {
            'categoria':'Categoria',
            'nome':'Nome',
            'descricao':'Descrição',
            'quantidade_estoque':'Quantidade'
            }

# form da Entrada
class EntradaForm(forms.ModelForm):
    fornecedor = forms.ModelChoiceField(queryset=Fornecedor.objects.all().order_by('nome'), empty_label='Selecione um fornecedor')
    produto = forms.ModelChoiceField(queryset=Produto.objects.all().order_by('nome'), empty_label='Selecione um produto')
    class Meta:
        model = EntradaProduto
        fields =[
            'fornecedor',
            'produto',
            'quantidade',
        ]
        # labels = {
        #     'fornecedor': '',
        #     'produto': '',
        #     'quantidade': '',
        # }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['forncedor'].widget.attrs.update(
                {
                    'placeholder':'Fornecedor',
                    'class':'col form-control my-2 p-2'
                }
            )
            self.fields['produto'].widget.attrs.update(
                {
                    'placeholder':'Produto',
                    'class':'col form-control my-2 p-2'
                }
            )
            self.fields['quantidade'].widget.attrs.update(
                {
                    'placeholder':'Quantidade',
                    'class':'col form-control my-2 p-2'
                }
            )
            
# form da Saida
class SaidaForm(forms.ModelForm):
    produto = forms.ModelChoiceField(queryset=Produto.objects.all().order_by('nome'), empty_label='Selecione um produto')
    class Meta:
        model = SaidaProduto
        fields =[
            'produto',
            'motivo',
            'quantidade',
        ]
        # labels = {
        #     'produto': '',
        #     'motivo': '',
        #     'quantidade': '',
        # }
        widgets = {'motivo':TextInput()}
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['produto'].widget.attrs.update(
                {
                    'placeholder':'Produto',
                    'class':'col form-control my-2 p-2'
                }
            )
            self.fields['motivo'].widget.attrs.update(
                {
                    'placeholder':'Motivo',
                    'class':'col form-control my-2 p-2'
                }
            )
            self.fields['quantidade'].widget.attrs.update(
                {
                    'placeholder':'Quantidade',
                    'class':'col form-control my-2 p-2'
                }
            )


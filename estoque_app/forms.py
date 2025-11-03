from django import forms
from .models import Categoria, Fornecedor

# form da Categoria
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']
        labels = {'nome': 'Nome', 'descricao': 'Descrição'}
        widgets = {'descricao': forms.Textarea(attrs={'cols': 80})}

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

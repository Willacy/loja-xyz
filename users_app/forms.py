from django import forms
from .models import Usuario
from django.forms.widgets import *
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):    
    class Meta:
        model = Usuario
        fields = ['nome', 'senha']
        labels = {'nome':'', 'senha':''}
        widgets = {'senha':PasswordInput()}
        help_texts = {'nome': None}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update(
                {
                    'placeholder':'Usuario',
                    'class':'col form-control my-2 p-2'
                }
            )
        self.fields['senha'].widget.attrs.update(
                {
                    'placeholder':'Senha',
                    'class':'col form-control my-2 p-2'
                }
            )
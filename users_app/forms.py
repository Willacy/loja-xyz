from django import forms
from django.forms.widgets import *
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username':'', 'password':''}
        widgets = {'password':PasswordInput()}
        help_texts = {'username': None}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
                {
                    'placeholder':'Usuario',
                    'class':'col form-control my-2 p-2'
                }
            )
        self.fields['password'].widget.attrs.update(
                {
                    'placeholder':'Senha',
                    'class':'col form-control my-2 p-2'
                }
            )
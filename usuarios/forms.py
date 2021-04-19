from django import forms
from usuarios.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('name','email', 'password')
        labels = {
            'name':'Name',
            'email' : 'Email',
            'password' : 'Password'

        }





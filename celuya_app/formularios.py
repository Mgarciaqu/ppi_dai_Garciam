from django import forms
from django.contrib.auth.forms import UserCreationForm
from .modelos import UsuarioPersonalizado

class FormularioCreacionUsuario(UserCreationForm):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'email', 'password1', 'password2')


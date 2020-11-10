from django import forms
from django.forms import ModelForm
from .models import producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class productosForm(ModelForm):

    class Meta:
        model = producto
        fields = ['codigoproducto', 'nombrep', 'preciop', 'descripcion', 'imagen']


class CustomUserForm(UserCreationForm):
    pass

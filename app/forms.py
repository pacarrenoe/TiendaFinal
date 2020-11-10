from django import forms
from django.forms import ModelForm
from .models import producto

class productosForm(ModelForm):

    class Meta:
        model = producto
        fields = ['codigoproducto', 'nombrep', 'preciop', 'descripcion', 'imagen']

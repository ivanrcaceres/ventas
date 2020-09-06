from cliente.models import Cliente
from django import forms

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'numerodedocumento', 'telefono']


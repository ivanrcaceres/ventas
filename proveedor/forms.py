from django import forms

from dal import autocomplete

from proveedor.models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'numerodedocumento', 'telefono']
        widgets = {
            "Proveedor": autocomplete.ModelSelect2(url='proveedor-autocomplete'),
        }
from django.contrib.auth.models import User
from cliente import autocomplete
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
from django import forms
from cliente.models import Cliente
from compra.models import Compra, DetalleCompra
from venta.models import Venta, DetalleVenta
from dal import autocomplete

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', ]
        widgets = {
            "proveedor": autocomplete.ModelSelect2(url='proveedor-autocomplete'),
        }

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ['producto', 'preciounitario', 'cantidad', 'subtotal']
        widgets = {
            "producto": autocomplete.ModelSelect2(url='producto-autocomplete'),
        }

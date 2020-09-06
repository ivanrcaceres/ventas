from django.contrib.auth.models import User
from cliente import autocomplete
from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
from django import forms
from cliente.models import Cliente
from venta.models import Venta, DetalleVenta
from dal import autocomplete

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', ]
        widgets = {
            "cliente": autocomplete.ModelSelect2(url='cliente-autocomplete'),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'preciounitario', 'cantidad', 'subtotal']
        widgets = {
            "producto": autocomplete.ModelSelect2(url='producto-autocomplete'),
        }


class VentaSearchForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=autocomplete.ModelSelect2(url='cliente-autocomplete',), required=False
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(url='user-autocomplete', ), required=False
    )
    #cliente = forms.ModelChoiceField(widget=autocomplete.ModelSelect2(url='cliente-autocomplete',), required=False)
    desde = forms.DateField(widget=AdminDateWidget(attrs={'placeholder':'Desde'}), required=False)
    hasta = forms.DateField(widget=AdminDateWidget(attrs={'placeholder':'Hasta'}), required=False, initial=datetime.now())
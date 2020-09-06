from producto.models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'codigo','cantidadenexistencia', 'preciodecompra']
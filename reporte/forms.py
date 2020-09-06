from django.contrib.admin.widgets import AdminDateWidget
from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from cliente.models import Cliente
from reporte.models import ReporteVenta
from dal import autocomplete

class ReporteVentaForm(forms.ModelForm):
    class Meta:
        model = ReporteVenta
        fields = '__all__'
    # class Media:
    #     js = ('reporte/reporteventa01.js',)




class VentaSearchForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        widget=autocomplete.ModelSelect2(url='cliente-autocomplete2',), required=False
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(url='user-autocomplete', ), required=False
    )
    # eliminado = (())
    ELIMINADOS = (
        ('Todas', 'Todas'),
        ('Eliminadas', 'Eliminadas'),
        ('No_eliminadas', 'No Eliminadas'),
    )

    # eliminado = forms.ModelChoiceField(ELIMINADOS, required=False)
    # eliminado = forms.BooleanField(choices=ELIMINADOS, required=False)
    eliminado = forms.ChoiceField(choices=ELIMINADOS, label="Ventas", initial='Todas', widget=forms.Select(), required=True)
    # eliminado = forms.CharField(choices=ELIMINADOS, required=False)
    # eliminado = forms.ModelChoiceField(
    #     queryset=ELIMINADOS, required=False
    # )


    #cliente = forms.ModelChoiceField(widget=autocomplete.ModelSelect2(url='cliente-autocomplete',), required=False)
    desde = forms.DateField(widget=AdminDateWidget(attrs={'placeholder':'Desde'}), required=False)
    hasta = forms.DateField(widget=AdminDateWidget(attrs={'placeholder':'Hasta'}), required=False, initial=datetime.now())

from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from compra.forms import DetalleCompraForm, CompraForm
from compra.models import DetalleCompra, Compra


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    form = DetalleCompraForm
    extra = 0


class CompraAdmin(admin.ModelAdmin):
    form = CompraForm
    inlines = [DetalleCompraInline]
    list_display = ['fecha', 'proveedor', 'eliminar']
    list_display_links = ['fecha', 'proveedor']
    list_per_page = 5

    def eliminar(self, obj):
        html = '&nbsp;&nbsp;<a  title="Eliminar" href="/admin/compra/compra/%s/delete">Eliminar </a>' % obj.pk
        return mark_safe(html)


admin.site.register(Compra, CompraAdmin)
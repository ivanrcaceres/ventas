from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from producto.forms import ProductoForm
from producto.models import Producto


class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm
    # inlines = [ContactoInline]
    list_display = ['nombre','codigo', 'cantidadenexistencia', 'Precio_de_venta','eliminar']
    list_display_links = ['nombre','codigo', 'cantidadenexistencia', 'Precio_de_venta']
    # list_display_links = []
    list_per_page = 5

    # admin.site.disable_action('delete_selected')

    def eliminar(self, obj):
        # http: // localhost:8000 / admin / facturacion / facturacion / 26 / delete /
        # html = '<a class="button" title="Agregar Pasajeros" href="/admin/embarque/embarque/%s/?pasajeros=1"> <i class="fa fa-user-plus"></i></a>&nbsp;&nbsp;' % obj.pk
        # html = '<a class="button" title="Eliminar" href="/admin/venta/venta/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;&nbsp;' % obj.pk
        # html = '&nbsp;&nbsp;<a class="button" title="Imprimir" href="/admin/producto/producto/%s/delete"></a>'%obj.pk
        html = '&nbsp;&nbsp;<a  title="Eliminar" href="/admin/producto/producto/%s/delete">Eliminar </a>' % obj.pk
        # html += '<a class="button" title="Eliminar" href="/admin/facturacion/facturacion/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i> <span class="sr-only"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo de</font></font></span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"></font></font></a>&nbsp;&nbsp;' % obj.pk
        return mark_safe(html)


    def get_queryset(self, request):
        qs = super(ProductoAdmin, self).get_queryset(request)
        qs = qs.filter(eliminado=False)
        return qs



admin.site.register(Producto, ProductoAdmin)
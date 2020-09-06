from django.contrib import admin
from django.utils.safestring import mark_safe
from venta.forms import DetalleVentaForm, VentaForm
from venta.models import DetalleVenta, Venta


class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    form = DetalleVentaForm
    extra = 0

    def get_queryset(self, request):
        qs = super(DetalleVentaInline, self).get_queryset(request)
        qs = qs.filter(eliminado=False)
        return qs


class VentaAdmin(admin.ModelAdmin):
    form = VentaForm
    inlines = [DetalleVentaInline]
    list_display = ['fecha', 'cliente', 'Pago', 'imprimir', 'eliminar']
    list_display_links = ['fecha', 'cliente']
    list_per_page = 5
    # search_fields = ['parabuscarci']

    # para eliminar la opcion de eliminar varios
    # admin.site.disable_action('delete_selected')

    # def parabuscarci(self):
    #     aux = self.id
    #     return int(aux)



    def eliminar(self, obj):
        # http: // localhost:8000 / admin / facturacion / facturacion / 26 / delete /
        # html = '<a class="button" title="Agregar Pasajeros" href="/admin/embarque/embarque/%s/?pasajeros=1"> <i class="fa fa-user-plus"></i></a>&nbsp;&nbsp;' % obj.pk
        # html = '<a class="button" title="Eliminar" href="/admin/venta/venta/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;&nbsp;' % obj.pk
        html = '&nbsp;&nbsp;<a  title="Eliminar" href="/admin/venta/venta/%s/delete">Eliminar </a>' % obj.pk
        # html += '<a class="button" title="Eliminar" href="/admin/facturacion/facturacion/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i> <span class="sr-only"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo de</font></font></span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"></font></font></a>&nbsp;&nbsp;' % obj.pk
        return mark_safe(html)

    def imprimir(self,obj):
        # html = '<a class="button" title="Agregar Pasajeros" href=""> <i class="fa fa-user-plus"></i></a>&nbsp;&nbsp;'
        # html += '<a class="button" title="Imprimir Lista de Pasajeros" href=""> <i class="fa fa-users"></i></a>'
        # html +=  '&nbsp;&nbsp;<a class="button" title="Imprimir Planilla de Trabajo" href=""> <i class="fa fa-file-pdf-o"></i></a>'
        # html += '&nbsp;&nbsp;<a class="button" title="Imprimir Presupuesto" href="/pdfloco/"> <i class="fa fa-file-pdf-o"></i></a>'
        # return mark_safe(html)

        html = '&nbsp;&nbsp;<a  title="ticket" href="/recibo/%s">Ticket</a>' % obj.pk
        html += '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a  title="factura" href="/factura/%s">Factura </a>' % obj.pk
        return mark_safe(html)

    def get_queryset(self, request):
        qs = super(VentaAdmin, self).get_queryset(request)
        qs = qs.filter(eliminado=False)
        return qs

admin.site.register(Venta, VentaAdmin)
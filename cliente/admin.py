from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from cliente.forms import ClienteForm
from cliente.models import Contacto, Cliente


class ContactoInline(admin.TabularInline):
    model = Contacto
    extra = 0

class ClienteAdmin(admin.ModelAdmin):
    form = ClienteForm
    inlines = [ContactoInline]
    list_display = ['nombre', 'numerodedocumento', 'telefono','eliminar']
    # list_display_links = ['nombre', 'numerodedocumento', 'telefono']
    list_display_links = []

    # class Media:
    #     css = {
    #         "all": (
    #             '/static/admin/css/jquery-ui.css',
    #             "/static/admin/orden_trabajo/ot_changeform.css",
    #         )
    #     }
    #     js = (
    #         # '/static/admin/js/jquery.js',
    #         '/static/admin/cliente/change_list.js',
    #     )





    def eliminar(self, obj):
        # http: // localhost:8000 / admin / facturacion / facturacion / 26 / delete /
        # html = '<a class="button" title="Agregar Pasajeros" href="/admin/embarque/embarque/%s/?pasajeros=1"> <i class="fa fa-user-plus"></i></a>&nbsp;&nbsp;' % obj.pk
        # html = '<a class="button" title="Eliminar" href="/admin/venta/venta/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i></a>&nbsp;&nbsp;' % obj.pk
        # html = '&nbsp;&nbsp;<a class="button" title="Imprimir" href="/admin/cliente/cliente/%s/delete"></a>'%obj.pk
        html = '&nbsp;&nbsp;<a  title="Eliminar" href="/admin/cliente/cliente/%s/delete">Eliminar </a>' % obj.pk
        # html += '<a class="button" title="Eliminar" href="/admin/facturacion/facturacion/%s/delete"> <i class="fa fa-trash" aria-hidden="true"></i> <span class="sr-only"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo de</font></font></span><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"></font></font></a>&nbsp;&nbsp;' % obj.pk
        return mark_safe(html)


    def get_queryset(self, request):
        qs = super(ClienteAdmin, self).get_queryset(request)
        qs = qs.filter(eliminado=False)
        return qs



admin.site.register(Cliente,ClienteAdmin)

admin.site.site_header = 'Sistema Venta'
admin.site.site_title = 'Sistema Venta'

admin.site.disable_action('delete_selected')
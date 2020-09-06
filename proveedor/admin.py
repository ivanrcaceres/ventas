from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from proveedor.forms import ProveedorForm
from proveedor.models import Proveedor, Contacto


class ContactoInline(admin.TabularInline):
    model = Contacto
    extra = 0

class ProveedorAdmin(admin.ModelAdmin):
    inlines = [ContactoInline]
    form = ProveedorForm
    list_display = ['nombre', 'numerodedocumento', 'telefono','eliminar']
    list_display_links = ['nombre', 'numerodedocumento', 'telefono']

    def eliminar(self, obj):
        html = '&nbsp;&nbsp;<a  title="Eliminar" href="/admin/proveedor/proveedor/%s/delete">Eliminar </a>' % obj.pk
        return mark_safe(html)

admin.site.register(Proveedor,ProveedorAdmin)
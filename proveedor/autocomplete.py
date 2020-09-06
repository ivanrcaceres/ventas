from dal import autocomplete
from proveedor.models import Proveedor


class ProveedorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Proveedor.objects.none()

        qs = Proveedor.objects.filter(eliminado=False)

        if self.q:
            qs = qs.filter(numerodedocumento__istartswith=self.q)
        return qs
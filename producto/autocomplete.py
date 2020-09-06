from dal import autocomplete
from producto.models import Producto


class ProductoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Producto.objects.none()

        # qs = Producto.objects.all()
        qs = Producto.objects.filter(eliminado=False)

        if self.q:
            qs = qs.filter(codigo__istartswith=self.q)

        return qs
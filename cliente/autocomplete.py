from dal import autocomplete


from cliente.models import Cliente


class ClienteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cliente.objects.none()

        # qs = Cliente.objects.all()
        qs = Cliente.objects.filter(eliminado=False)

        if self.q:
            qs = qs.filter(numerodedocumento__istartswith=self.q)

        return qs

class ClienteAutocomplete2(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Cliente.objects.none()

        qs = Cliente.objects.all()
        # qs = Cliente.objects.filter(eliminado=False)

        if self.q:
            qs = qs.filter(numerodedocumento__istartswith=self.q)

        return qs
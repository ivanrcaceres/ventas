from django.contrib.auth.models import User

from dal import autocomplete


# from cliente.models import Cliente


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return User.objects.none()

        qs = User.objects.all()
        # qs = User.objects.filter(eliminado=False)

        if self.q:
            qs = qs.filter(username__istartswith=self.q)

        return qs
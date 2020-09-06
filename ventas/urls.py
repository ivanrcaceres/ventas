"""ventas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from cliente.autocomplete import ClienteAutocomplete, ClienteAutocomplete2
from cliente.views import datodelcliente
from producto.autocomplete import ProductoAutocomplete
from producto.views import productosajax, productosajax2
from proveedor.autocomplete import ProveedorAutocomplete
from venta.autocomplete import UserAutocomplete
from venta.views import ventasreportes01, ventasreportes02, ventasreportes03, recibopdf, facturapdf

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^cliente-autocomplete/$',
        ClienteAutocomplete.as_view(),
        name='cliente-autocomplete',
    ),

    # ClienteAutocomplete2
    url(
        r'^cliente-autocomplete2/$',
        ClienteAutocomplete2.as_view(),
        name='cliente-autocomplete2',
    ),

    url(
        r'^producto-autocomplete/$',
        ProductoAutocomplete.as_view(),
        name='producto-autocomplete',
    ),
    url(
        r'^user-autocomplete/$',
        UserAutocomplete.as_view(),
        name='user-autocomplete',
    ),

    url(
        r'^proveedor-autocomplete/$',
        ProveedorAutocomplete.as_view(),
        name='proveedor-autocomplete',
    ),

    url(
        r'^ventasreportes01/(?P<dia1>\d+)/(?P<mes1>\d+)/(?P<ano1>\d+)/(?P<dia2>\d+)/(?P<mes2>\d+)/(?P<ano2>\d+)/(?P<username1>\w+)/(?P<cliente1>\S+)/(?P<elimina2>\w+)/$',
        ventasreportes01,
        ),

    url(
        r'^ventasreportes02/(?P<dia1>\d+)/(?P<mes1>\d+)/(?P<ano1>\d+)/(?P<dia2>\d+)/(?P<mes2>\d+)/(?P<ano2>\d+)/(?P<username1>\w+)/(?P<cliente1>\S+)/(?P<elimina2>\w+)/$',
        ventasreportes02,
        ),

    url(
        r'^ventasreportes03/(?P<dia1>\d+)/(?P<mes1>\d+)/(?P<ano1>\d+)/(?P<dia2>\d+)/(?P<mes2>\d+)/(?P<ano2>\d+)/(?P<username1>\w+)/(?P<cliente1>\S+)/(?P<elimina2>\w+)/$',
        ventasreportes03,
        ),

    # AJAX
    url(r'^datodelcliente/', datodelcliente, name='datodelcliente'),
    url(r'^productosajax/', productosajax,name='productosajax'),
    url(r'^productosajax2/', productosajax2,name='productosajax2'),

    # TICKET O FACTURA
    url(
        r'^recibo/(?P<id>\d+)/$',
        recibopdf,
        ),

    url(
        r'^factura/(?P<id>\d+)/$',
        facturapdf,
        ),


]

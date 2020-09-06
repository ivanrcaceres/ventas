from django.contrib import admin
from reporte.forms import VentaSearchForm
from reporte.models import ReporteDetalleVenta, ReporteVenta
import datetime

class ReporteDetalleVentaInline(admin.TabularInline):
    model = ReporteDetalleVenta
    #form = DetalleVentaForm
    extra = 0

class ReporteVentaAdmin(admin.ModelAdmin):
    # form = VentaForm
    inlines = [ReporteDetalleVentaInline]
    list_display = ['fecha', 'cliente','eliminado']
    list_display_links = ['fecha', 'cliente']
    list_per_page = 5
    # class Media:
    #     js = ('reporte/reporteventa01.js',)



    def get_queryset(self, request):
        form = self.advanced_search_form
        qs = super(ReporteVentaAdmin, self).get_queryset(request)
        print form
        print '###################'
        print 'desde'
        print form.cleaned_data.get('desde')
        print 'hasta'
        print form.cleaned_data.get('hasta')
        print 'cliente'
        print form.cleaned_data.get('cliente')
        print 'user'
        print form.cleaned_data.get('user')
        print 'todas?'
        print form.cleaned_data.get('eliminado')

        cuales = form.cleaned_data.get('eliminado')


        if(cuales == 'Todas' or cuales == None ):
            print 'Todas'
        elif(cuales == 'Eliminadas'):
            print 'Eliminadas'
            qs = qs.filter(eliminado=True)
        else:
            print 'No Eliminadas'
            qs = qs.filter(eliminado=False)

            # print form.cleaned_data['cliente']
            # qs = qs.filter(cliente_id=form.cleaned_data['cliente'])


        if form.cleaned_data['cliente']:
            print form.cleaned_data['cliente']
            qs = qs.filter(cliente_id=form.cleaned_data['cliente'])

        if form.cleaned_data['user']:
            print form.cleaned_data['user']
            qs = qs.filter(user_id=form.cleaned_data['user'])

        if form.cleaned_data['desde']:
            print form.cleaned_data['desde']
            desdeaux = str(form.cleaned_data['desde'])+' 00:00:00'
            print desdeaux
            qs = qs.filter(fecha__gte=desdeaux)
        if form.cleaned_data['hasta']:
            print 'hasta'
            x = datetime.datetime.now()
            print x
            fecha = str(form.cleaned_data['hasta'])
            print fecha
            ano = fecha[:4]
            print ano
            mes = fecha[5:7]
            print mes
            dia = fecha[8:10]
            print dia
            hora = '23'
            print hora
            minuto = '59'
            print minuto
            segundo = '59'
            print segundo
            mile = '59'
            print mile

            fechah = ano+'-'+mes+'-'+dia+' '+hora+':'+minuto+':'+segundo



            qs = qs.filter(fecha__lte=fechah)

        # print form.cleaned_data['cliente']
        # print '###################'
        # print 'entra en el get_queryset'
        # qs = qs.filter(eliminado=True)

        return qs
    def changelist_view(self, request, extra_context=None, **kwargs):

        self.my_request_get = request.GET.copy()
        self.advanced_search_form = VentaSearchForm(request.GET)
        self.advanced_search_form.is_valid()
        self.other_search_fields = {}
        extra_context = extra_context or {}
        extra_context.update({'asf': VentaSearchForm,
                              'my_request_get':self.my_request_get,
                              })
        request.GET._mutable = True

        for key in self.advanced_search_form.fields.keys():
            try:
                temp = request.GET.pop(key)
            except KeyError:
                pass
            else:
                if temp != ['']:
                    self.other_search_fields[key] = temp
        request.GET_mutable = False

        desde = request.GET.get('desde', '')
        hasta = request.GET.get('hasta', '')

        # return lista_ventas_pdf(request=request, queryset=self.get_queryset(request=request), desde=desde, hasta=hasta)


        #OBs:
        # este estaba asi antes que ivan cambie
        # return super(VentaAdmin, self) \
        #     .changelist_view(request, extra_context=extra_context, **kwargs)

        # despues que ivan cambio
        print 'entra en el segundooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo'
        return super(ReporteVentaAdmin, self).changelist_view(request, extra_context=extra_context, **kwargs)


admin.site.register(ReporteVenta, ReporteVentaAdmin)
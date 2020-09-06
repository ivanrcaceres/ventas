from __future__ import unicode_literals
from django import template
from django.contrib.admin.templatetags.admin_list import result_headers, result_hidden_fields, results
from django.contrib.admin.views.main import SEARCH_VAR


register = template.Library()


def advanced_search_form(context, cl):
    """
    Displays a search form for searching the list.
    """
    form = context.get('asf')
    form = form(data=context.get('my_request_get'))
    return {
        'asf' : form,
        'cl': cl,
        'request':context.get('request',''),
        'panel':context.get('panel',''),
        'show_result_count': cl.result_count != cl.full_result_count,
        'search_var': SEARCH_VAR
    }

@register.inclusion_tag('admin/reporte/reporteventa/venta_search_form.html', takes_context=True)
def venta_search_form(context, cl):
   return advanced_search_form(context,cl)
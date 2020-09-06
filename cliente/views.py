from django.http.response import JsonResponse
from cliente.models import Cliente
import json

def datodelcliente(request):
    datos = request.GET.getlist('valor')
    datos_list = json.loads(datos[0])
    cliente = Cliente.objects.get(numerodedocumento=datos_list[0])
    vectorcondp2 = [cliente.id]
    return JsonResponse({'vector': vectorcondp2})
from django.shortcuts import render
import json
from django.http.response import JsonResponse


# Create your views here.
from producto.models import Producto
# Create your views here.
def productosajax(request):

    # estos estas dos lineas deben ir juntos
    datos = request.GET.getlist('valor')
    datos_list = json.loads(datos[0])


    print 'ajajajajajajajajajja'
    print datos_list
    print 'ajajajajajajajajajja'
    print datos_list[0]
    #
    #
    # # data = request.GET['valor']
    # data = request.GET['valor']
    #
    # print 'datos:'
    # print datos
    # print 'datos_list[0]:'
    # print datos_list[0]
    # print 'datos_list:'
    # print datos_list
    # print 'data:'
    # print data
    # print 'vector: '
    #
    c = 0
    for au in datos_list:
        print 'los datos'
        print au
        c = c + 1
    print c
    # print '-------------------------------'
    vector = []
    productos = Producto.objects.all()
    for au in datos_list:
        for au2 in productos:
            if au == au2.codigo:
                vector.append(au2.precio)
    #     for au2 in productos:
    #         if au == au2.codigo:
    #             vector.append(au2.precioventa)
    #
    # for i in vector:
    #     print 'i:'
    #     print i

    print vector

    # vector = ['ivan', 'tatty', 'kiki']

    return JsonResponse({'vector': vector})

def productosajax2(request):

    # estos estas dos lineas deben ir juntos
    datos = request.GET.getlist('valor')
    datos_list = json.loads(datos[0])


    print 'ajajajajajajajajajja'
    print datos_list
    print 'ajajajajajajajajajja'
    print datos_list[0]
    #
    #
    # # data = request.GET['valor']
    # data = request.GET['valor']
    #
    # print 'datos:'
    # print datos
    # print 'datos_list[0]:'
    # print datos_list[0]
    # print 'datos_list:'
    # print datos_list
    # print 'data:'
    # print data
    # print 'vector: '
    #
    c = 0
    for au in datos_list:
        print 'los datos'
        print au
        c = c + 1
    print c
    # print '-------------------------------'
    vector = []
    productos = Producto.objects.all()
    for au in datos_list:
        for au2 in productos:
            if au == au2.codigo:
                vector.append(au2.preciodecompra)
    #     for au2 in productos:
    #         if au == au2.codigo:
    #             vector.append(au2.precioventa)
    #
    # for i in vector:
    #     print 'i:'
    #     print i

    print vector

    # vector = ['ivan', 'tatty', 'kiki']

    return JsonResponse({'vector': vector})
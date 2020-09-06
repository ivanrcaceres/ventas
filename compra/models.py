from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Compra(models.Model):
#     fecha =
from producto.models import Producto
from proveedor.models import Proveedor


class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, null=True,blank=True)
    eliminado = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        return str(self.proveedor.nombre)

    # def __unicode__(self):
    #     return self.proveedor.nombre + ', '+self.Pago()
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if(self.id != None):
            detallecompras = DetalleCompra.objects.filter(compra=self.id)
            for dc in detallecompras:
                producto = Producto.objects.get(pk=dc.producto.id)
                producto.cantidadenexistencia = producto.cantidadenexistencia - int( dc.cantidad )
                producto.save()
        super(Compra, self).save()

    def delete(self, using=None):
        # los detalles compras de la venta
        detallecompras = DetalleCompra.objects.filter(compra=self.id)

        listap = []

        for i in detallecompras:
            producto = Producto.objects.get(pk=i.producto.id)

            # aqui cargo los productos de la compra
            listap.append(producto.id)

            aux1 = int(producto.cantidadenexistencia)
            aux2 = int(i.cantidad)
            aux3 = aux1-aux2
            producto.cantidadenexistencia = aux3
            producto.save()

        super(Compra, self).delete()
        for j in listap:
            detallecompras2 = DetalleCompra.objects.filter(producto=j).order_by('-id')
            producto = Producto.objects.get(pk=j)

            print detallecompras2

            if(len(detallecompras2) == 0):
                print 'vacio'
                producto.preciodecompra = 0
            else:
                producto.preciodecompra = int(detallecompras2[0].preciounitario.replace(".", "").replace(".", "").replace(".", "").replace(".", "").replace(".", ""))
            producto.save()

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto)
    preciounitario = models.CharField('Precio unitario',max_length=100)
    cantidad = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=120)
    eliminado = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # print self.producto
        producto = Producto.objects.get(pk = self.producto.id)
        # print producto
        aux1 = producto.cantidadenexistencia
        aux2 = self.cantidad
        aux3 = int(aux1)+int(aux2)
        # print aux1
        # print aux2
        # print aux3

        producto.cantidadenexistencia = aux3
        precionuevo = self.preciounitario.replace(".", "").replace(".", "").replace(".", "").replace(".", "").replace(".", "").replace(".", "")
        print 'el nuevo precio es '+ precionuevo
        producto.preciodecompra = precionuevo
        producto.save()
        super(DetalleCompra, self).save()
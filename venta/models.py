from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cliente.models import Cliente
from producto.models import Producto
from reporte.models import ReporteVenta, ReporteDetalleVenta


class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    cliente = models.ForeignKey(Cliente)
    eliminado = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)

    # def __unicode__(self):
    #     return self.id

    def __unicode__(self):
        return self.cliente.nombre

    def Pago(self):
        print self.id

        a = suma(self.id)
        print a

        return str(a)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if(self.id == None):
            u = User.objects.values()
            print u[0].get('username')
            u2 = u[0].get('id')
            u3 = User.objects.get(pk=u2)
            self.user = u3
            super(Venta, self).save()
            rv = ReporteVenta(fecha=self.fecha, cliente=self.cliente, eliminado=self.eliminado, user=self.user)
            rv.save()
        else:

            detalleventas = DetalleVenta.objects.filter(venta=self.id)
            for dv in detalleventas:
                producto = Producto.objects.get(pk=dv.producto.id)
                producto.cantidadenexistencia = int(producto.cantidadenexistencia) + int(dv.cantidad)
                producto.save()

            super(Venta, self).save()
            rv = ReporteVenta.objects.get(pk=self.id)
            rv.fecha=self.fecha
            rv.cliente=self.cliente
            rv.eliminado=self.eliminado
            rv.user=self.user
            rv.save()

    def delete(self, using=None):
        self.eliminado = True
        self.save()
        rv = ReporteVenta.objects.get(pk=self.id)
        rv.eliminado = True
        rv.save()


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta)
    producto = models.ForeignKey(Producto)
    preciounitario = models.CharField('Precio unitario',max_length=100)
    cantidad = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=120)
    eliminado = models.BooleanField(default=False)


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # if(self.id==None):
        print 'self.venta.id'
        print self.venta_id
        rv = ReporteVenta.objects.get(pk=self.venta_id)
        rdv = ReporteDetalleVenta(venta=rv, producto=self.producto,
                                  preciounitario=self.preciounitario,
                                  cantidad=self.cantidad, subtotal=self.subtotal,
                                  eliminado=self.eliminado)
        rdv.save()
        super(DetalleVenta, self).save()
        # aqui editamos producto
        producto = Producto.objects.get(id=self.producto.id)
        producto.cantidadenexistencia = int(producto.cantidadenexistencia) - int(self.cantidad)
        producto.save()

        # else:
        #     super(DetalleVenta, self).save()
    def delete(self, using=None):

        detalleventas = DetalleVenta.objects.filter(venta=self.id)
        # print detalleventas
        for i in detalleventas:
            producto = Producto.objects.get(pk=i.producto.id)
            aux1 = int(producto.cantidaddeexistencia)
            aux2 = int(i.cantidad)
            aux3 = aux1 + aux2
            producto.cantidadenexistencia = aux3
            producto.save()


        rdv = ReporteDetalleVenta.objects.get(pk=self.id)
        rdv.eliminado = True
        rdv.save()
        super(DetalleVenta, self).delete()


def suma(dato):
    dv = DetalleVenta.objects.filter(venta=dato)
    suma = 0
    for i in dv:
        suma = suma + int(i.subtotal)

    suma = separador_de_miles(str(suma))

    return suma


def separador_de_miles(numero):
    v = str(numero).split(".")
    s = v[0]
    for i in range(len(v[0]), 0, -3):
        s = s[:i] + s[i:] if i == 1 and s[0] == "-" else s[:i] + "." + s[i:]
    a = s[:len(s) - 1]
    # if gs:
    #    return a

    if len(v) == 2 and v[1] != "00":
        dato = v[1][0:2] if len(v[1]) > 2 else v[1]
        a += "," + dato
    return a
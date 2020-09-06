from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from cliente.models import Cliente
from producto.models import Producto



class ReporteVenta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True,blank=True)
    eliminado = models.BooleanField(default=False)
    user = models.ForeignKey(User, blank=True, null=True)


class ReporteDetalleVenta(models.Model):
    venta = models.ForeignKey(ReporteVenta)
    producto = models.ForeignKey(Producto)
    preciounitario = models.CharField('Precio unitario',max_length=100)
    cantidad = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=120)
    eliminado = models.BooleanField(default=False)
    # detalleventa = models.ForeignKey(DetalleVenta)

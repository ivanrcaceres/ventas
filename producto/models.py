from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=120, unique=True)
    precio = models.IntegerField('Precio de venta')
    preciodecompra = models.IntegerField('precio de compra',default=0)
    eliminado = models.BooleanField(default=False)
    cantidadenexistencia = models.IntegerField('cantidad en existencia', default=0)

    def __unicode__(self):
        return self.nombre + ', cod: '+self.codigo

    def delete(self, using=None):
        self.eliminado = True
        self.save()


    def Precio_de_venta(self):
        # print self.id

        a = separador_de_miles(str((self.precio)))
        print a

        return str(a)



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
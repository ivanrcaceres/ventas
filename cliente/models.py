from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField('Nombre',max_length=120)
    numerodedocumento = models.CharField('Numero de documento', max_length=120, unique=True)
    telefono = models.CharField('Telefono',max_length=120)
    eliminado = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nombre +' Nro. Doc.: ' +self.numerodedocumento

    def delete(self, using=None):
        self.eliminado = True
        self.save()

class Contacto(models.Model):
    ficha = models.ForeignKey(Cliente)
    nombre = models.CharField(max_length=120)
    telefono = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=120)
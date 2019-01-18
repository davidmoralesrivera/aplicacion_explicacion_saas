# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=100)

class Profesion(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(blank=True, null=True)
	categoria = models.ForeignKey(Categoria, blank=True, null=True)
# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	altura = models.IntegerField()
	genero = models.CharField(max_length=20, blank=True, null=True)
	profesion = models.ForeignKey(Profesion, blank=True, null=True)
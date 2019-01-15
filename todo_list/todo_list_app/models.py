# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Lista(models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=200)
	descripcion = models.TextField(blank=True, null=True)
	def get_terminadas(self):
		return self.tarea_set.filter(terminada=True).count()

	def get_total_tareas(self):
		return self.tarea_set.all().count()

class Tarea(models.Model):
	descripcion = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	terminada = models.BooleanField(default=False)
	lista = models.ForeignKey(Lista)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Noticia(models.Model):
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	autor = models.CharField(max_length=200)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
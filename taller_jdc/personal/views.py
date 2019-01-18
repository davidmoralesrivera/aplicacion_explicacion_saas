# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from personal.models import Persona

# Create your views here.

def personas(request):
	lista_personas = Persona.objects.all()
	return render(request, 'personas.html', locals())

def crear_persona(request):
	lista_personas = Persona.objects.all()
	if request.GET.get("nombre"):
		print request.GET.get("nombre")
	return render(request, 'personas.html', locals())
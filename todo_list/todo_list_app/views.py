# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import logout

from django.shortcuts import render,redirect

from todo_list_app.models import Tarea, Lista
from todo_list_app.forms import ListaForm
# Create your views here.

class HomeView(View,LoginRequiredMixin):
	login_url = '/iniciar_sesion/'
	def get(self, request):
		listas = Lista.objects.all()
		return render(request, "home.html", locals())

class CrearListaView(View,LoginRequiredMixin):
	login_url = '/iniciar_sesion/'

	def get(self, request):
		formulario = ListaForm()
		return render(request, "crear_lista.html", locals())
	def post(self, request):
		formulario = ListaForm(request.POST)
		if formulario.is_valid():
			lista = formulario.save(commit=False)
			lista.usuario = request.user
			lista.save()
		return redirect("/")

class TareasView(View,LoginRequiredMixin):
	login_url = '/iniciar_sesion/'

	def get(self, request):
		if request.GET.get("lista"):
			lista = Lista.objects.get(pk=request.GET.get("lista"))
		return render(request, "lista_tareas.html", locals())

	def post(self, request):
		lista = Lista.objects.get(pk=request.POST.get("lista"))
		tarea = Tarea(descripcion=request.POST.get("nueva_tarea"), lista=lista)
		tarea.save()
		return render(request, "fila_tarea.html", locals())

class TerminarTareaView(View,LoginRequiredMixin):
	login_url = '/iniciar_sesion/'

	def post(self, request):
		tarea = Tarea.objects.select_related("lista").get(pk=request.POST.get("tarea"))
		tarea.terminada = request.POST.get("terminada") == 'true'
		tarea.save()
		return HttpResponse("%d de %d" % (tarea.lista.get_terminadas(), tarea.lista.get_total_tareas()))

class LoginView(TemplateView):
	template_name = "login.html"
	def post(self, request):
		
		return redirect('/inicio/')

### auth

def cerrar_sesion(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect("/")
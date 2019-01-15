# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.contrib.auth import logout

from django.shortcuts import render,redirect

from noticias.models import * 

# Create your views here.

class LandingPageView(View):
	def get(self, request):
		noticias = Noticia.objects.all()
		return render(request, "landing.html", locals())
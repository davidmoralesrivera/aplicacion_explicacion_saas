# -*- coding: utf-8 -*-
import datetime, time
from django import forms
from django.utils import formats
from django.conf import settings
from todo_list_app.models import *
import json

class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        exclude = ["tareas", "usuario"]
        labels = {
        	"nombre":"Nombre",
        	"descripcion": "Descripción"
        }
        widgets = {
        	"nombre": forms.TextInput(attrs={"class":"form-control","autocomplete":"off"}),
        	"descripcion": forms.Textarea(attrs={"class":"form-control"})
        }
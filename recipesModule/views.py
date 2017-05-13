# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .addRecipesForm import AddRecipe

# Create your views here.
def inicio(request):
	form = AddRecipe()
	context = {"el_form": form}
	return render(request, "inicio.html", context)

def inicio_plantilla(request):
	return render(request, "index.html")
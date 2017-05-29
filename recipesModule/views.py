# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .addRecipesForm import AddRecipe
from models import Recipe

# Create your views here.
def inicio(request):
	form = AddRecipe()
	context = {"el_form": form}
	return render(request, "inicio.html", context)

def inicio_plantilla(request):
	query_recipes = Recipe.objects.all()
	context = {"query_recipes": query_recipes}
	return render(request, "index.html", context)

def recipes(request):
	return render(request, "recipes.html")

def contact(request):
	return render(request, "contact.html")

def login(request):
	return render(request, "login.html")
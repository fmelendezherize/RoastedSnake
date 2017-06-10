# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .addRecipesForm import AddRecipe
from models import Recipe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


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

def login_user(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				inicio_plantilla(request)
	return render(request, 'login.html')

def recipes_create(request):
	if request.POST:
		newRecipe = Recipe()
		newRecipe.name = request.POST['name']
		newRecipe.short_description = request.POST['short_description']
		newRecipe.category = request.POST['category']
		newRecipe.country =  request.POST['country']
		newRecipe.preparation_time = request.POST['preparation_time']
		newRecipe.cook_time = request.POST['cook_time']
		newRecipe.ingredients = request.POST['ingredients']
		newRecipe.directions = request.POST['directions']
		newRecipe.photo = request.POST['photo']
		newRecipe.save()
		inicio_plantilla(request)
	return render(request, "add.html")

def recipes_update():
	print "hola"

def recipes_delete():
	print "hola"

def recipe_get(request):
	if request.POST:
		if request.POST['action'] == "delete_recipe":
			print "hago delete a: " + request.POST['recipe_id']
			return redirect('inicio_plantilla')
	else:
		recipe_id = request.GET['id']
		query_recipe = Recipe.objects.get(pk=recipe_id)
		context = {"query_recipe": query_recipe}
		return render(request, "single_recipe.html", context)
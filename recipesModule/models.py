# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.

#CUSTOM CLASSES

#CUSTOM para guardar imagenes
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

#CUSTOM Relacion Padre-Hijo entre Recipe - Ingredientes. Una receta puede tener muchos ingredientes
class Ingredient(models.Model):
	single = models.CharField(max_length=200, blank=False, null=False)

	def __unicode__(self):
		return self.single

#CUSTOM Relacion Padre-Hijo entre Recipe - Directions. Una receta puede tener muchos direcciones
class Direction(models.Model):
	step = models.TextField()

	def __unicode__(self):
		return self.step


class Recipe(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	short_description = models.CharField(max_length=200, blank=False, null=False)
	category =  models.CharField(max_length=100, blank=False, null=False)
	country =  models.CharField(max_length=100, blank=False, null=False)
	preparation_time = models.IntegerField()
	cook_time = models.IntegerField()
	#ingredients = models.ForeignKey(Ingredient)
	#directions = models.OneToOneField(Direction)
	ingredients = models.TextField()
	directions = models.TextField()
	photo = models.ImageField() #CUSTOM Pide instalar Pillow
	creation_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

	def __unicode__(self):
		return self.name #CUSTOM El objeto retorna por defecto el Nombre de la receta al ser llamado por funciones
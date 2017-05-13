# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Recipe
from .models import Ingredient
from .models import Direction

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Direction)
from django.contrib import admin

from ingredients.models import Ingredient, Unit


admin.site.register(Unit)
admin.site.register(Ingredient)

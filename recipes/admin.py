from django.contrib import admin

from recipes.models import Recipe, RecipeIngredient


admin.site.register(Recipe)
admin.site.register(RecipeIngredient)

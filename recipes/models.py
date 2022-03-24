from django.db import models

from ingredients.models import Ingredient


class Recipe(models.Model):
    name = models.CharField(null=False, max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def total_cost(self):
        return sum([ri.cost() for ri in self.recipeingredient_set.all()])


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)

    def cost(self):
        return self.amount * self.ingredient.cost

    def __str__(self):
        return self.recipe.name

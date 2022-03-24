from django import forms

from recipes.models import RecipeIngredient, Recipe


# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ('name',)


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ('recipe', 'ingredient', 'amount')

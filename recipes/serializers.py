from rest_framework import serializers

from .models import Recipe, RecipeIngredient


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'
        depth = 3


# class RecipeIngredientShallowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecipeIngredient
#         fields = '__all__'

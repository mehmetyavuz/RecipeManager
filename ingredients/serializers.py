from rest_framework import serializers

from .models import Ingredient, Unit


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['name']


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'article_number', 'unit', 'amount', 'cost']

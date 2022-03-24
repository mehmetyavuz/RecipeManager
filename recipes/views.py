from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from recipes.models import Recipe


def index(request):
    recipe_list = Recipe.objects.order_by('name')
    context = {'recipe_list': recipe_list}
    return render(request, 'recipes/index.html', context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/detail.html', {'recipe': recipe})


def add_edit(request, recipe_id=None):
    if request.method == 'POST':
        new_name = request.POST['name']
        new_amount = request.POST['amount']
        if recipe_id:
            recipe = Recipe.objects.get(id=recipe_id)
            recipe.name = new_name
        else:
            recipe = Recipe(name=new_name)
        recipe.save()
        return HttpResponseRedirect(reverse('recipes:detail', args=(recipe.id,)))
    else:
        recipe = Recipe
        if recipe_id:
            recipe = Recipe.objects.get(id=recipe_id)

        return render(request, 'recipes/add_edit.html', {'recipe': recipe})

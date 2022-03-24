from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import RecipeSerializer, RecipeIngredientSerializer
from .models import Recipe, RecipeIngredient


@csrf_exempt
def recipes(request):
    if request.method == 'GET':
        all_units = Recipe.objects.all()
        serializer = RecipeSerializer(all_units, many=True,
                                      context={'request', request})
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def recipe_ingredients(request, recipe_id):
    if request.method == 'GET':
        all_objs = RecipeIngredient.objects.filter(recipe_id=recipe_id)
        serializer = RecipeIngredientSerializer(all_objs, many=True,
                                                context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecipeIngredientSerializer(data=data,
                                                context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recipe_ingredient(request, pk):
    try:
        obj = RecipeIngredient.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecipeIngredientSerializer(obj, data=data,
                                                context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

# def index(request):
#     recipe_list = Recipe.objects.order_by('name')
#     context = {'recipe_list': recipe_list}
#     return render(request, 'recipes/index.html', context)
#
#
# def detail(request, recipe_id):
#     recipe = get_object_or_404(Recipe, pk=recipe_id)
#     return render(request, 'recipes/detail.html', {'recipe': recipe})
#
#
# def add_edit(request, recipe_id=None):
#     if request.method == 'POST':
#         new_name = request.POST['name']
#         if recipe_id:
#             recipe = Recipe.objects.get(id=recipe_id)
#             recipe.name = new_name
#         else:
#             recipe = Recipe(name=new_name)
#         recipe.save()
#         return HttpResponseRedirect(reverse('recipes:detail', args=(recipe.id,)))
#     else:
#         recipe = Recipe
#         if recipe_id:
#             recipe = Recipe.objects.get(id=recipe_id)
#
#         return render(request, 'recipes/add_edit.html', {'recipe': recipe})

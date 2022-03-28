from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from ingredients.models import Ingredient
from .serializers import RecipeSerializer, RecipeIngredientSerializer
from .models import Recipe, RecipeIngredient


@csrf_exempt
def recipes(request):

    if request.method == 'GET':
        all_units = Recipe.objects.all()
        serializer = RecipeSerializer(all_units, many=True,
                                      context={'request', request})
        return JsonResponse(serializer.data, safe=False)

    elif request.method =='POST' or request.method == 'PUT':
        data = JSONParser().parse(request)

        if request.method == 'POST':
            serializer = RecipeSerializer(data=data,
                                          context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

        elif request.method == 'PUT':
            obj = Recipe.objects.get(pk=data['id'])
            serializer = RecipeSerializer(obj,
                                          data=data,
                                          context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def recipe(request, recipe_id):
    if request.method == 'DELETE':
        try:
            obj = Recipe.objects.get(pk=recipe_id)
            obj.delete()
            return HttpResponse(status=204)
        except:
            return HttpResponse(status=404)


@csrf_exempt
def recipe_ingredients(request, recipe_id):
    if request.method == 'GET':
        all_objs = RecipeIngredient.objects.filter(recipe_id=recipe_id)
        serializer = RecipeIngredientSerializer(all_objs, many=True,
                                                context={'request': request})
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def update_recipe_ingredients(request, recipe_id):
    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
            data_ids = []
            for d in data:
                if 'id' in d.keys():
                    data_ids.append(d['id'])
                    ri = RecipeIngredient.objects.get(id=d['id'])
                    if ri:
                        ri.amount = d['amount']
                        ri.save()
                else:
                    # create new one
                    recipe = Recipe.objects.get(id=d['recipe']['id'])
                    ingredient = Ingredient.objects.get(id=d['ingredient']['id'])
                    new_ri = RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient=ingredient,
                        amount=d['amount']
                    )
                    new_ri.save()
                    data_ids.append(new_ri.id)

            # delete removed ingredients
            RecipeIngredient.objects.filter(recipe_id=recipe_id).exclude(pk__in=data_ids).delete()

            all_objs = RecipeIngredient.objects.filter(recipe_id=recipe_id)
            serializer = RecipeIngredientSerializer(all_objs, many=True,
                                                    context={'request': request})
            return JsonResponse(serializer.data, safe=False)

        except Exception as e:
            return HttpResponse(e, status=404)
        # return JsonResponse(serializer.errors, status=400, safe=False)
    # elif request.method == 'DELETE':
    #     obj.delete()
    #     return HttpResponse(status=204)

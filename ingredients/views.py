from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .serializers import IngredientSerializer, UnitSerializer
from .models import Ingredient, Unit


@csrf_exempt
def units(request):
    if request.method == 'GET':
        all_units = Unit.objects.all()
        serializer = UnitSerializer(all_units, many=True,
                                    context={'request', request})
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def ingredients(request):
    if request.method == 'GET':
        all_objs = Ingredient.objects.all()
        serializer = IngredientSerializer(all_objs, many=True,
                                          context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IngredientSerializer(data=data,
                                          context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def ingredient(request, pk):
    try:
        obj = Ingredient.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IngredientSerializer(obj, data=data,
                                          context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

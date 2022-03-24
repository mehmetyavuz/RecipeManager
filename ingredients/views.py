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

# def index(request):
#     ingredient_list = Ingredient.objects.order_by('name')
#     context = {'ingredient_list': ingredient_list}
#     return render(request, 'ingredients/index.html', context)
#
#
# def detail(request, ingredient_id):
#     ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
#     return render(request, 'ingredients/detail.html', {'ingredient': ingredient})
#
#
# def edit(request, ingredient_id):
#     if request.method == 'POST':
#         i = Ingredient.objects.get(pk=ingredient_id)
#         f = IngredientForm(request.POST, instance=i)
#         f.save()
#         return HttpResponseRedirect(reverse('ingredients:detail', args=(i.id,)))
#     else:
#         ingredient = get_object_or_404(Ingredient, pk=ingredient_id)
#         f = IngredientForm(instance=ingredient)
#
#         return render(request, 'ingredients/add_edit.html', {'ingredient_form': f})
#
#
# def add(request):
#     if request.method == 'POST':
#         f = IngredientForm(request.POST)
#         f.save()
#         return HttpResponseRedirect(reverse('ingredients:detail', args=(f.instance.id,)))
#     else:
#         f = IngredientForm()
#         return render(request, 'ingredients/add_edit.html', {'ingredient_form': f})

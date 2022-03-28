from django.urls import path

from recipes import views

app_name = 'recipes'
urlpatterns = [
    path('recipes/', views.recipes),
    path('recipe/<int:recipe_id>/', views.recipe),
    path('<int:recipe_id>/', views.recipe_ingredients),
    path('update/<int:recipe_id>/', views.update_recipe_ingredients),
]
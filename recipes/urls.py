from django.urls import path

from recipes import views

app_name = 'recipes'
urlpatterns = [
    # path('', views.recipe_ingredients),
    path('recipes/', views.recipes),
    path('<int:recipe_id>/', views.recipe_ingredients),

    # path('', views.index, name='index'),
    # path('add/', views.add_edit, name='add'),
    # path('<int:recipe_id>/', views.detail, name='detail'),
    # path('<int:recipe_id>/edit', views.add_edit, name='edit'),
]
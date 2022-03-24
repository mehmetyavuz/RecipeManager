from django.urls import path

from ingredients import views

app_name = 'ingredients'
urlpatterns = [
    path('', views.ingredients),
    path('units/', views.units),
    path('<int:pk>/', views.ingredient),

    # path('', views.index, name='index'),
    # path('add/', views.add, name='add'),
    # path('<int:ingredient_id>/', views.detail, name='detail'),
    # path('<int:ingredient_id>/edit', views.edit, name='edit'),
]

from django.urls import path

from ingredients import views

app_name = 'ingredients'
urlpatterns = [
    path('', views.ingredients),
    path('units/', views.units),
    path('<int:pk>/', views.ingredient),
]

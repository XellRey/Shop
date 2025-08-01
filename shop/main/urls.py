from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('pizza/', views.pizza, name='pizza'),
    path('coffe/', views.coffe, name='coffe'),
    path('drinks/', views.drinks, name='drinks'),
    path('desserts/', views.desserts, name='desserts'),
    path('sauce/', views.sauce, name='sauce'),

]
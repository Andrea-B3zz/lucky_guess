from django.urls import path
from . import views

urlpatterns = [
    path('newnumber', views.newNumber, name='newNumber'),
    path('newgame', views.newGame, name='newGame'),
]
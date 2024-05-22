from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.login, name='register'),
    path('personal', views.login, name='personal'),
]
from django.urls import path
from .views import home,create_todo

urlpatterns = [
        path('', home, name='home'),
        path('create', create_todo, name='create-todo')
    ]
from django.urls import path
from .views import home,create_todo,Listview,update

urlpatterns = [
        path('', home, name='home'),
        path('create', create_todo, name='create-todo'),
        path('show',Listview,name="show"),
        path('update/<int:id>',update,name="update"),
    ]
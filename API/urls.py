from django.urls import path
from . import views


from . import views
urlpatterns = [
         path('', views.Todo_view.as_view(),name='api'),
        path('create', views.create_todo, name='create-todo'),
        path('show',views.Listview,name="show"),
        path('update',views.update,name="update"),
        path('delete/<str:uid>',views.delete,name="delete"),
       

        

        
    ]


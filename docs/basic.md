## Django Rest Framework

## what is Django Rest Framework?
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:
to build your own Web APIs.
to integrate Web APIs into your Django projects.
to build browsable APIs for your development and testing needs.

## steps 
1. install django and rest framework
2. create a new project
3. create a new app

**django file system**
    
```bash
    ├── db.sqlite3
    ├── manage.py
    ├── project
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-37.pyc
    │   │   ├── settings.cpython-37.pyc
    │   │   ├── urls.cpython-37.pyc
    │   │   └── wsgi.cpython-37.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    |── apps

```
**apps file system**

```bash
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-37.pyc
    │   └── admin.cpython-37.pyc
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── __init__.py
    │   └── __pycache__
    │       └── __init__.cpython-37.pyc
    ├── models.py
    ├── tests.py
    └── views.py
```
create new api app
```bash
    python manage.py startapp api
```
-Add your app to the project settings.py file
```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'api.apps.ApiConfig',
    ]
```
configure URLS of the project
```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', include('api.urls')),
    ]
```
create new urls.py file in the api app
```python
    from django.urls import path
    from .views import home

    urlpatterns = [
        path('', home, name='home'),
    ]
```
create new views.py file in the api app
```python
    from django.shortcuts import render
    from django.http import HttpResponse

    def home(request):
        return HttpResponse('Hello World')
```


        

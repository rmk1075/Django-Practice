# Django-Practice

## 1. Init Django Project

### install django

#### create virtualenv

```shell
$ python -m venv venv
```

#### install django code

```shell
$ python -m pip install Django
```

- <https://docs.djangoproject.com/en/6.0/topics/install/#installing-an-official-release-with-pip>

```shell
$ pip list

Package  Version
-------- -------
asgiref  3.11.0
Django   6.0
pip      25.3
sqlparse 0.5.4
```

### django project

#### create django project

```shell
$ django-admin startproject myproject .
```

- <https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-a-project>

##### django-admin

- <https://docs.djangoproject.com/en/6.0/ref/django-admin/>

#### project structure

```shell
Django-Practice
├── manage.py
└── myproject
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

#### run django server

```shell
$ python manage.py runserver
```

## 2. Init Django Application

### django application

#### create django application

```shell
# create app "hello"
$ python manage.py startapp hello
```

- <https://docs.djangoproject.com/en/6.0/intro/tutorial01/#creating-the-polls-app>

#### application structure

```shell
hello
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

#### create Hello World api

```python
# hello/views.py

# create hello_world function
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("Hello World")
```

```python
# hello/urls.py

# create hello/urls.py for url configuration for app 'hello'
# add '/world' url configuration
from django.urls import path

from . import views

urlpatterns = [
    path("world", views.hello_world, name="world"),
]
```

```python
# myproject/urls.py

# add '/hello' url configuration to root urls.py
# include(...) references url configuration in hello.urls module 
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls'))
]
```

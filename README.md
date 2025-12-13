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

## 3. Create Django Model

### django model

#### define model

```python
# hello/models.py
from django.db import models

class Greeting(models.Model):
    country = models.CharField(max_length=100)
    greeting = models.CharField(max_length=100)
```

#### include app

```python
# myproject/settings.py
INSTALLED_APPS = [
    'hello.apps.HelloConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

#### makemigrations

```shell
$ python manage.py makemigrations hello

Migrations for 'hello':
  hello/migrations/0001_initial.py
    + Create model Greeting
```

#### sqlmigrate

```shell
$ python manage.py sqlmigrate hello 0001

BEGIN;
--
-- Create model Greeting
--
CREATE TABLE "hello_greeting" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "country" varchar(100) NOT NULL, "greeting" varchar(100) NOT NULL);
COMMIT;
```

#### migrate

```shell
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, hello, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying hello.0001_initial... OK
  Applying sessions.0001_initial... OK
```

## 4. Model Query

### model manager

#### objects

```python
# django.db.models.base.pyi
class Model(metaclass=ModelBase):
    # ...

    _default_manager: ClassVar[BaseManager[Self]]
    objects: ClassVar[BaseManager[Self]]

    # ...
```

#### custom manager

```python
from django.db import models


class KoreaManager(models.Manager):
    def get_kr(self):
        return self.get(country="KR")

class Greeting(models.Model):
    objects = models.Manager() # default manager
    korea = KoreaManager() # custom manager

    # ...
```

### objects query

#### create object

```python
# save()
greeting = Greeting(country="KR", greeting="안녕하세요")
greeting.save()

# create()
Greeting.objects.create(country="US", greeting="Hello")
```

#### update object

```python
hello = Greeting.objects.get(country="US")
hello.greeting = "Hi"
hello.save()
```

#### retrieve object

```python
# all
Greeting.objects.all()

# filter
Greeting.objects.filter(greeting="Hello")

# get
Greeting.objects.get(country="KR")
```

#### delete object

```python
# delete
hello = Greeting.objects.get(country="US")
hello.delete()

# delete all
Greeting.objects.all().delete()
```

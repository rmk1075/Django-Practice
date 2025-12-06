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

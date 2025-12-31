from django.urls import path

from . import views

urlpatterns = [
    path("", views.HelloView.as_view(), name="hello"),
    path("world", views.hello_world, name="world"),
    path("init", views.init_greetings, name="init")
]

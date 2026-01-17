from django.urls import path

from . import views

urlpatterns = [
    path("", views.HelloView.as_view(), name="hello"),
    # path("world", views.hello_world, name="hello-world"),
    path("world", views.HelloWorldView.as_view(), name="hello-world-view"),
    path("init", views.init_greetings, name="hello-init")
]

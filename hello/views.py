from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from hello.models import GREETINGS_MAP, Greeting


def hello_world(request):
    return HttpResponse("Hello World")


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello World")


def init_greetings(request):
    created_greetings = []
    for country, greeting in GREETINGS_MAP.items():
        obj, created = Greeting.objects.get_or_create(
            country=country,
            defaults={"greeting": greeting}
        )

        if created:
            created_greetings.append({"country": obj.country, "greeting": obj.greeting})

    return HttpResponse(content=created_greetings)


class PostHelloRequest:
    def __init__(self, request):
        self.country = request.POST.get("country")
        self.greeting = request.POST.get("greeting")


class HelloView(View):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        result = [{"country": greeting.country, "greeting": greeting.greeting} for greeting in Greeting.objects.all()]
        return render(request, "hello.html", {"result": result})

    def post(self, request, *args, **kwargs) -> JsonResponse:
        post_hello_request = PostHelloRequest(request)
        obj, created = Greeting.objects.get_or_create(
            country=post_hello_request.country,
            defaults={"greeting": post_hello_request.greeting}
        )

        message = f"[country={obj.country} greeting={obj.greeting}]"
        message += " is created." if created else " already exists."
        result = [{"country": greeting.country, "greeting": greeting.greeting} for greeting in Greeting.objects.all()]
        return render(request, "hello.html", {"result": result, "created": message})

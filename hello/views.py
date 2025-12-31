from django.http import HttpResponse

from hello.models import GREETINGS_MAP, Greeting


def hello_world(request):
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

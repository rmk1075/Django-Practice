from django.test import TestCase

from hello.models import Greeting


GREETINGS_MAP = {
    "KR": "안녕하세요",
    "US": "Hello",
    "JP": "こんにちは",
    "FR": "Bonjour",
    "DE": "Guten Tag",
    "ES": "Hola",
    "IT": "Ciao",
    "GB": "Hello",
}

class TestModels(TestCase):
    def test_greeting_crud(self):
        # create objects
        for k, v in GREETINGS_MAP.items():
            greeting = Greeting(country=k, greeting=v)
            greeting.save()

        # retrieve objects
        greetings = Greeting.objects.all()
        self.assertEqual(len(greetings), len(greetings_map))

        for greeting in greetings:
            self.assertEqual(greeting.greeting, greetings_map.get(greeting.country))

        # update objects
        hello = Greeting.objects.get(country="US")
        hello.greeting = "Hi"
        hello.save()

        self.assertEqual(Greeting.objects.get(country="US").greeting, "Hi")

        # delete objects
        Greeting.objects.all().delete()
        self.assertEqual(len(Greeting.objects.all()), 0)

    def test_custom_manager(self):
        for k, v in GREETINGS_MAP.items():
            greeting = Greeting(country=k, greeting=v)
            greeting.save()

        greeting = Greeting.korea.get_kr()
        self.assertEqual(greeting.greeting, GREETINGS_MAP.get("KR"))


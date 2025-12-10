from django.test import TestCase

from hello.models import Greeting


class TestModels(TestCase):
    def test_greeting_crud(self):
        greetings_map = {
            "KR": "안녕하세요",
            "US": "Hello",
            "JP": "こんにちは",
            "FR": "Bonjour",
            "DE": "Guten Tag",
            "ES": "Hola",
            "IT": "Ciao",
            "GB": "Hello",
        }

        # create objects
        for k, v in greetings_map.items():
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

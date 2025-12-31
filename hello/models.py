from django.db import models


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

class KoreaManager(models.Manager):
    def get_kr(self):
        return self.get(country="KR")

class Greeting(models.Model):
    objects = models.Manager()
    korea = KoreaManager()

    country = models.CharField(max_length=100)
    greeting = models.CharField(max_length=100)

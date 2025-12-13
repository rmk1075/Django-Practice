from django.db import models

class KoreaManager(models.Manager):
    def get_kr(self):
        return self.get(country="KR")

class Greeting(models.Model):
    objects = models.Manager()
    korea = KoreaManager()

    country = models.CharField(max_length=100)
    greeting = models.CharField(max_length=100)

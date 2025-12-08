from django.db import models

class Greeting(models.Model):
    country = models.CharField(max_length=100)
    greeting = models.CharField(max_length=100)

import random
from django.core.cache import cache
from django.test import TestCase


class TestSettings(TestCase):
    def test_caching(self):
        l = [random.randint(0, 100) for _ in range(100)]

        for k, v in enumerate(l):
            cache.set(k, v)

        for k, v in enumerate(l):
            self.assertEqual(cache.get(k), v)



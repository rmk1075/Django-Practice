import random
from django.conf import settings
from django.core.cache import cache, caches
from django.test import TestCase


class TestSettings(TestCase):
    def test_caching(self):
        l = [random.randint(0, 100) for _ in range(100)]

        for k, v in enumerate(l):
            cache.set(k, v)

        for k, v in enumerate(l):
            self.assertEqual(cache.get(k), v)

    def test_filesystem_cache(self):
        l = [random.randint(0, 100) for _ in range(100)]

        cache = caches['file_cache']
        cache.clear()

        for k, v in enumerate(l):
            cache.set(k, v)

        for k, v in enumerate(l):
            self.assertEqual(cache.get(k), v)

        cache.clear()

    def test_filesystem_cache_entry(self):
        size = 300
        l = [random.randint(0, 100) for _ in range(size)]

        cache = caches['file_cache']
        cache.clear()

        for k, v in enumerate(l):
            cache.set(k, v)

        for k, v in enumerate(l):
            self.assertEqual(cache.get(k), v)

        cache.set(size + 1, random.randint(0, 100))

        number_of_none = 0
        for k, v in enumerate(l):
            if cache.get(k) is None:
                number_of_none += 1

        self.assertEqual(number_of_none, int((size + 1) / settings.FILE_CACHE_CULL_FREQUENCY))

        cache.clear()

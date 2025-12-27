from myproject.settings.base import *

SETTINGS_MODE = "TEST"

"""
- MAX_ENTRIES:  The maximum number of entries allowed in the cache before old values are deleted. This argument defaults to 300.
- CULL_FREQUENCY:  The fraction of entries that are culled when MAX_ENTRIES is reached. The actual ratio is 1 / CULL_FREQUENCY. This argument should be an integer and defaults to 3.
"""
FILE_CACHE_MAX_ENTRIES = 300
FILE_CACHE_CULL_FREQUENCY = 3

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
    "file_cache": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "django_cache" / "file_cache",
        "OPTIONS": {
            "MAX_ENTRIES": FILE_CACHE_MAX_ENTRIES,
            "CULL_FREQUENCY": FILE_CACHE_CULL_FREQUENCY,
        }
    },
    "redis_cache": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

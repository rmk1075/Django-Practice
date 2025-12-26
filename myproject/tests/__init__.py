import django
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings.test")
django.setup()

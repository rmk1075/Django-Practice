from django.conf import settings
from django.test import TestCase


class TestSettings(TestCase):
    def test_id_debug(self):
        if settings.DEBUG:
            print("DEBUG MODE")

    def test_settings_mode(self):
        self.assertEqual(settings.SETTINGS_MODE, "TEST")

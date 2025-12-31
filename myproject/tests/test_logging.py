import logging
from django.conf import settings
from django.test import TestCase


logger = logging.getLogger(__name__)
console_debug_logger = logging.getLogger("console_debug")
file_debug_logger = logging.getLogger("file_debug")
console_info_with_format_logger = logging.getLogger("console_info_with_format")

class TestLoggings(TestCase):
    def setUp(self):
        with open(settings.DEBUG_LOG_FILE, "w"):
            pass

    def test_root_logger(self):
        logger.debug("debug") # skipped
        logger.info("info") # skipped
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")

    def test_console_debug_logger(self):
        console_debug_logger.debug("debug")
        console_debug_logger.info("info")
        console_debug_logger.warning("warning")
        console_debug_logger.error("error")
        console_debug_logger.critical("critical")

    def test_file_debug_logger(self):
        file_debug_logger.debug("debug")
        file_debug_logger.info("info")
        file_debug_logger.warning("warning")
        file_debug_logger.error("error")
        file_debug_logger.critical("critical")

        with open(settings.DEBUG_LOG_FILE, "r") as f:
            self.assertEqual(f.readline().strip(), "debug")
            self.assertEqual(f.readline().strip(), "info")
            self.assertEqual(f.readline().strip(), "warning")
            self.assertEqual(f.readline().strip(), "error")
            self.assertEqual(f.readline().strip(), "critical")

    def test_console_debug_with_format_logger(self):
        console_info_with_format_logger.debug("debug")
        console_info_with_format_logger.info("info")
        console_info_with_format_logger.warning("warning")
        console_info_with_format_logger.error("error")
        console_info_with_format_logger.critical("critical")

    def test_console_loggers(self):
        loggers = [logger, console_debug_logger, console_info_with_format_logger]
        for l in loggers:
            l.debug("debug")
            l.info("info")
            l.warning("warning")
            l.error("error")
            l.critical("critical")

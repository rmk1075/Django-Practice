import logging
from django.test import TestCase


logger = logging.getLogger(__name__)

class TestLoggings(TestCase):
    def test_logger(self):
        logger.debug("debug")
        logger.info("info")
        logger.warning("warning")
        logger.error("error")
        logger.critical("critical")
        
        

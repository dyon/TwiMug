import unittest
from TwiMug import ConfigurationService


class TestConfigurationService(unittest.TestCase):

    def setUp(self):
        self.config = ConfigurationService.ConfigurationService()

    def test_read_key_value(self):
        value = self.config.read_key_value("Twitter", "ConsumerKey")

        self.assertTrue(len(value) > 0)

    def test_read_config(self):
        self.assertTrue(self.config.read_config())

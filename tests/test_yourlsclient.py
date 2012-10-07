import unittest
from TwiMug import YourlsClient

API_KEY = "XXXXXXXXXX"
ENDPOINT = "http://example.com/yourls-api.php"


class TestYourlsClient(unittest.TestCase):

    def setUp(self):
        self.yourlsclient = YourlsClient.YourlsClient(API_KEY, ENDPOINT)

    def test_get_short_url(self):
        short_url = self.yourlsclient.get_short_url("http://testurl.com")

        self.assertTrue(len(short_url) > 0)

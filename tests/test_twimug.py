import unittest
from TwiMug import TwiMug


class TestTwiMug(unittest.TestCase):

    def setUp(self):
        self.twimug = TwiMug.TwiMug()

    def test_main_application(self):
        self.twimug.post_to_twitter()

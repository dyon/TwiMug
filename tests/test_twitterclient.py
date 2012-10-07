import unittest
from datetime import datetime
from TwiMug import TwitterClient


CONSUMER_KEY = "XXXXXXXXXX"
CONSUMER_SECRET = "XXXXXXXXXX"

ACCESS_TOKEN = "XXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXX"


class TestTwitterClient(unittest.TestCase):

    def setUp(self):
        self.twitterclient = TwitterClient.TwitterClient(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = self.twitterclient.get_api()

    def test_twitter_connect(self):
        self.assertTrue(len(self.api.me().name))

    def test_tweet(self):
        self.assertTrue(self.twitterclient.tweet("Test TwiMug " + str(datetime.today())))

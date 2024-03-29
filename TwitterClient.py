import tweepy


class TwitterClient:

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def get_api(self):
        return self.api

    def tweet(self, text):
        try:
            self.api.update_status(text)
        except Exception, e:
            raise

        return True

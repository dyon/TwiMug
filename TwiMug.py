import ConfigurationService
import TwitterClient
import SmugMugClient
import YourlsClient


class TwiMug:

    def __init__(self):
        # Read the configuration file
        self.config = ConfigurationService.ConfigurationService()
        self.smugmug = SmugMugClient.SmugMugClient(self.config.read_key_value('SmugMug', 'ApiKey'), \
                                                   self.config.read_key_value('SmugMug', 'Gallery'), \
                                                   self.config.read_key_value('SmugMug', 'LinkType'), \
                                                   self.config.read_key_value('SmugMug', 'Nickname'))
        self.twitter = TwitterClient.TwitterClient(self.config.read_key_value('Twitter', 'ConsumerKey'), \
                                                   self.config.read_key_value('Twitter', 'ConsumerSecret'), \
                                                   self.config.read_key_value('Twitter', 'AccessToken'), \
                                                   self.config.read_key_value('Twitter', 'AccessTokenSecret'))
        self.yourls = YourlsClient.YourlsClient(self.config.read_key_value('YOURLS', 'ApiKey'), \
                                                self.config.read_key_value('YOURLS', 'Endpoint'))

    def post_to_twitter(self):
        # First we get the last image original url and his caption
        image_url = self.smugmug.get_last_image_url()

        # We check if the image has been previously tweeted
        if image_url == self.smugmug.load_last_image_url():
            return False

        caption = self.smugmug.get_last_image_extended_info()["Caption"]

        # Then, we'll shorten the url using our custom YOURLS installation
        short_url = self.yourls.get_short_url(image_url)

        # Finally, compose the tweet and send it!
        if len(short_url) > 0:
            tweet = "{0} {1}".format(caption, short_url) if len(caption) > 0 else short_url
            self.twitter.tweet(tweet)

            # We save the link
            self.smugmug.save_last_image_url()

            return True

        return False

tm = TwiMug()

tm.post_to_twitter()


import urllib


class YourlsClient:

    def __init__(self, api_key, endpoint):
        self.api_key = api_key
        self.endpoint = endpoint

    def get_short_url(self, url):
        short_url = ""

        f = urllib.urlopen("{0}?signature={1}&action=shorturl&format=simple&url={2}".format(self.endpoint, self.api_key, url))
        short_url = f.read()

        return short_url


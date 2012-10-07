import unittest
from TwiMug import SmugMugClient


API_KEY = "XXXXXXXXXX"
GALLERY = "XXXXXXXXXX"
LINK_TYPE = "LightboxURL"
NICKNAME = "XXXXXXXXXX"


class TestSmugMugClient(unittest.TestCase):

    def setUp(self):
        self.smugmugclient = SmugMugClient.SmugMugClient(API_KEY, GALLERY, LINK_TYPE, NICKNAME)
        self.albums = self.smugmugclient.get_albums()

    def test_retrieve_albums(self):
        self.assertTrue(len(self.albums) > 0)

    def test_specific_album_exists(self):
        for album in self.albums["Albums"]:
            if album["Title"] == GALLERY:
                return

        self.fail("Specific album not found.")

    def test_album_has_images(self):
        for album in self.albums["Albums"]:
            if album["Title"] == GALLERY:
                images = self.smugmugclient.get_images_for_album(album["id"], album["Key"])

                self.assertTrue(len(images) > 0)

                return

        self.fail("Album is empty.")

    def test_get_image_urls_is_greater_than_zero(self):
        last_image = self.smugmugclient.get_last_image_info()
        urls = self.smugmugclient.get_image_urls(last_image["id"], last_image["Key"])

        self.assertTrue(len(urls) > 0)

    def test_get_last_image_urls_is_greater_than_zero(self):
        url = self.smugmugclient.get_last_image_urls()

        self.assertTrue(len(url) > 0)

    def test_get_last_image_url(self):
        url = self.smugmugclient.get_last_image_url()

        self.assertTrue(len(url) > 0)

    def test_save_last_image_url(self):
        url = self.smugmugclient.get_last_image_url()

        self.smugmugclient.save_last_image_url()

        self.assertEquals(self.smugmugclient.load_last_image_url(), url)

    def test_get_last_image_caption(self):
        last_image = self.smugmugclient.get_last_image_extended_info()

        self.assertTrue(last_image["Caption"] > 0)


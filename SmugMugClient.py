from smugpy import SmugMug


class SmugMugClient:

    def __init__(self, api_key, gallery, link_type, nickname):
        self.smugmug = SmugMug(api_key=api_key, api_version="1.3.0", app_name="TwiMug")
        self.gallery = gallery
        self.link_type = link_type
        self.nickname = nickname

    def get_albums(self):
        albums = self.smugmug.albums_get(NickName=self.nickname)

        return albums

    def get_album_info(self, album_name):
        for album in self.get_albums()["Albums"]:
            if album["Title"] == album_name:
                return album

    def get_images_for_album(self, album_id, album_key):
        images = self.smugmug.images_get(AlbumID=album_id, AlbumKey=album_key)

        return images

    def get_image_urls(self, image_id, image_key):
        urls = self.smugmug.images_getURLs(ImageID=image_id, ImageKey=image_key)

        return urls

    def get_last_image_urls(self):
        last_image = self.get_last_image_info()
        urls = self.get_image_urls(last_image["id"], last_image["Key"])

        return urls

    def get_last_image_info(self):
        album = self.get_album_info(self.gallery)
        images = self.get_images_for_album(album["id"], album["Key"])
        last_image = images["Album"]["Images"][-1]

        return last_image

    def get_last_image_extended_info(self):
        last_image = self.get_last_image_info()
        extended_info = self.smugmug.images_getInfo(ImageID=last_image["id"], ImageKey=last_image["Key"])

        return extended_info["Image"]

    def get_last_image_url(self):
        urls = self.get_last_image_urls()

        return urls["Image"][self.link_type]

    def save_last_image_url(self):
        url = self.get_last_image_url()

        with open("last_image_url", "w") as file:
            file.write(url)

    def load_last_image_url(self):
        url = ""

        with open("last_image_url", "r") as file:
            url = file.readline()

        return url


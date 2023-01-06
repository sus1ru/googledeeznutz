import requests as req
import pyimgbox
from settings import MySettings


class BackEngine:
    api_key = MySettings.api_key
    search_result_count = MySettings.default_result_count

    @staticmethod
    def UpdateBackEngine():
        BackEngine.api_key = MySettings.api_key
        BackEngine.search_result_count = MySettings.default_result_count

    @staticmethod
    async def img_up(path):
        async with pyimgbox.Gallery(title="Hello, World!") as gallery:
            async for submission in gallery.add(path):
                if not submission['success']:
                    # print(f"{submission['filename']}: {submission['error']}")
                    return "Something went wrong..."
                else:
                    return submission['image_url']


class EngineForVolumes(BackEngine):
    def __init__(self, search_url):
        super().__init__()
        self.search_url = search_url

    def search_vols(self, search_text):
        res = {}
        self.UpdateBackEngine()
        if search_text == "":
            return res
        try:
            query = search_text
            params = {
                "q": query,
                "maxResults": BackEngine.search_result_count,
                "projection": "lite",
                "key": BackEngine.api_key
            }
            res = req.get(self.search_url, params=params).json()
        except:
            res = {}

        return res


class EngineForSpecificVolume(BackEngine):
    def __init__(self, search_url):
        super().__init__()
        self.search_url = search_url

    def search_vol(self, vol_id):
        res = {}
        self.UpdateBackEngine()
        if vol_id == "":
            return res
        try:
            self.search_url = f"{self.search_url}/{vol_id}"
            params = {
                "projection": "full",
                "key": BackEngine.api_key
            }
            res = req.get(self.search_url, params=params).json()
        except:
            res = {}

        return res


# myengine = BackEngine("AIzaSyBbPP24ydzOKh-abcnOr-spr-Y8GiCEYVA")
# res = myengine.search_vols("intitle:frankenstein+inauthor:shelley")
# print(type(res))
# print(res)

# fl_json = open('vol.json', "r")
# book_list = json.loads(fl_json.read())
# fl_json.close()

# url = 'http://books.google.com/books/content?id=LapIzQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'

import requests as req


class SearchDetails:
    def __init__(self, book_details):
        super().__init__()
        self.id = book_details["id"]
        self.title = book_details["volumeInfo"]["title"]
        self.authors = book_details["volumeInfo"].get("authors", [])
        self.authors_f = ', '.join(self.authors) if len(self.authors) else 'NA'
        self.published_date = book_details["volumeInfo"].get(
            "publishedDate", "NA"
        )
        self.thumbnail_link = book_details["volumeInfo"].get(
            "imageLinks", {}
        ).get(
            "thumbnail", "/persistent/default_cover.jpg"
        )
        self.cover_img_path = f"/persistent/default_cover.jpg"

    def GetImage(self):
        if self.thumbnail_link == "":
            return
        try:
            # print(self.thumbnail_link)
            path = f"/cache/{self.id}.jpg"
            res = req.get(self.thumbnail_link, allow_redirects=True)
            with open(path, 'wb') as img:
                img.write(res.content)
        except:
            self.cover_img_path = "/persistent/default_cover.jpg"
        else:
            self.cover_img_path = f"/cache/{self.id}.jpg"


class SearchDetailsSpecific:
    def __init__(self, book_details_lite, book_details_json):
        super().__init__()
        self.book_details_lite = book_details_lite
        self.subtitle = book_details_json["volumeInfo"].get(
            "subtitle", ""
        )
        self.description = book_details_json["volumeInfo"].get(
            "description", "NA"
        )
        self.publisher = book_details_json["volumeInfo"].get("publisher", "NA")
        self.page_count = book_details_json["volumeInfo"].get(
            "pageCount", "NA")
        isbn = book_details_json["volumeInfo"].get("industryIdentifiers", [])
        self.isbn13 = "NA"
        for val in isbn:
            if val["type"] == "ISBN_13":
                self.isbn13 = val["identifier"]
        self.book_link = book_details_json["volumeInfo"].get(
            "previewLink", "NA"
        )
# fl_json = open('vol.json', "r")
# book_list = json.loads(fl_json.read())
# fl_json.close()

# url = 'http://books.google.com/books/content?id=LapIzQEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'

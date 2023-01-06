from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, Image, ImageFit,
    ShaderMask, BlendMode, RadialGradient, animation, TextStyle
)
from flet.transform import Scale
from searchdetails import SearchDetailsSpecific
from bookdetails import BookDetails
from backengine import EngineForSpecificVolume
from settings import MySettings
from modals import InfoContainer


class BookCard(UserControl):
    def __init__(self, book_details_lite):
        super().__init__()
        self.book_details_lite = book_details_lite
        self.book_details = None
        self.my_engine = EngineForSpecificVolume(
            r'https://www.googleapis.com/books/v1/volumes')
        # self.book_details_dialog = book_details_dialog
        # self.page.dialog = self.book_details_dialog
        self.api_key = MySettings.api_key
        self.default_result_count = MySettings.default_result_count
        self.label = "settings"
        self.my_colors = [
            colors.TRANSPARENT,
            "#303030",
            "#3f3f46",
        ]
        # print(the_book.id)
        # print(len(self.the_books))

    def scaleUp(self, x):
        if x.control.scale != 1.1:
            x.control.scale = 1.1
        else:
            x.control.scale = 1

        x.control.update()

    def bookselect(self, e):
        if self.book_details == None:
            self.book_details_json = self.my_engine.search_vol(
                self.book_details_lite.id)
            self.book_details = SearchDetailsSpecific(
                self.book_details_lite, self.book_details_json)

        book_details_dialog = BookDetails(self.book_details)
        self.page.dialog = book_details_dialog
        book_details_dialog.OpenForm()
        self.update()
        self.page.update()

    def build(self):
        self.BookContainer = Card(
            # return Card(
            elevation=12,
            content=Container(
                # Animation
                on_click=self.bookselect,
                on_hover=lambda x: self.scaleUp(x),
                scale=Scale(scale=1),
                animate_scale=animation.Animation(1200, "bounceOut"),
                content=Stack(
                    controls=[
                        Image(
                            src=self.book_details_lite.thumbnail_link,
                            width=320,
                            # height=100,
                            fit=ImageFit.COVER,
                            border_radius=border_radius.all(16),
                        ),
                        Container(
                            border_radius=border_radius.all(16),
                            gradient=RadialGradient(
                                center=Alignment(0.4, -0.8),
                                radius=1.8,
                                # the self.colors in this case is the list of colors from the pyhton dictioanry
                                colors=self.my_colors,
                            ),
                        ),
                        Container(
                            padding=padding.all(10),
                            content=Column(
                                alignment="end",
                                spacing=0,
                                controls=[
                                    InfoContainer(
                                          title=self.book_details_lite.title,
                                          size=11,
                                          weight='w700',
                                          color='#d7ccc9',
                                          width=156,
                                          alignment=alignment.center_left
                                    ),
                                    Row(
                                        alignment='spaceBetween',
                                        controls=[
                                            InfoContainer(
                                                title=self.book_details_lite.authors_f,
                                                size=10,
                                                weight='w600',
                                                color='#c2dee1',
                                                width=76,
                                                alignment=alignment.bottom_left
                                            ),
                                            InfoContainer(
                                                title=self.book_details_lite.published_date,
                                                size=10,
                                                weight='w600',
                                                color='#dcedc1',
                                                width=68,
                                                alignment=alignment.bottom_right
                                            ),
                                        ],
                                    ),
                                ]
                            ),
                        ),
                    ],
                ),
            ),
        )
        return self.BookContainer

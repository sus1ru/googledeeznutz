from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, Image, ImageFit,
    ShaderMask, BlendMode, RadialGradient, animation, TextStyle
)
from searchdetails import SearchDetails
from bookcard import BookCard
from backengine import EngineForVolumes


class HomePage(UserControl):
    def __init__(self):
        super().__init__()
        self.label = "home"
        self.my_engine = EngineForVolumes(
            r'https://www.googleapis.com/books/v1/volumes')
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

    def GridGenerator(self):
        for bk in self.the_books:
            # threading.Thread(target=bk.GetImage, daemon=True).start()
            BookContainer = BookCard(bk)
            # print(BookContainer)
            self.BookColumn.controls.append(BookContainer)
            # self.BookColumn.update()
        self.BookColumn.update()

    def GridClear(self):
        self.BookColumn.controls.clear()
        self.BookColumn.update()

    def GridInit(self, search_text):
        self.GridClear()
        self.the_books = []
        books_details_json = self.my_engine.search_vols(search_text)
        for bk in books_details_json["items"]:
            the_book = SearchDetails(bk)
            self.the_books.append(the_book)
        self.GridGenerator()

    def MainContainer(self):
        def SearchBarHandle(e):
            if len(e.control.value) < 3:
                self.SearchIcon.disabled = True
            else:
                self.SearchIcon.disabled = False

            self.update()

        self.BookColumn = GridView(
            padding=padding.all(4),
            expand=1,
            runs_count=2,
            # max_extent=150,
        )
        self.SearchIcon = IconButton(
            icon=icons.SEARCH_ROUNDED,
            icon_size=16,
            disabled=True,
            on_click=lambda e: self.GridInit(self.SearchBar.value),
        )
        self.SearchBar = TextField(
            value="",
            height=30,
            prefix_icon=icons.SEARCH,
            text_style=TextStyle(size=14, weight="w300"),
            content_padding=padding.symmetric(3, 0),
            border_color=colors.TRANSPARENT,
            border_radius=border_radius.all(16),
            filled=True,
            on_change=SearchBarHandle,
        )
        self.main_container = Container(
            width=420,
            height=744,
            border_radius=border_radius.all(12),
            padding=padding.only(16, 8, 16, 72),
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["#222121", "#303030"],
            ),
            content=Column(
                controls=[
                    Row(
                        alignment="spaceBetween",
                        controls=[
                            self.SearchBar,
                            Container(
                                content=Row(
                                    alignment="end",
                                    spacing=0,
                                    controls=[
                                        self.SearchIcon,
                                        IconButton(
                                            icon=icons.CLEAR_OUTLINED,
                                            icon_size=16,
                                            on_click=lambda e: self.GridClear(),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    self.BookColumn,
                ],
            ),
        )
        return self.main_container

    def build(self):
        return Column(
            controls=[
                self.MainContainer(),
            ]
        )

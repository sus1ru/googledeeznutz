from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, Image, ImageFit,
    ShaderMask, BlendMode, RadialGradient, animation, TextStyle, TextButton
)
from modals import CopyInfoField, InfoContainer, ImageUploadField
import html2text


class BookDetails(UserControl):
    def __init__(self, book_details):
        super().__init__()
        self.my_colors = [
            colors.TRANSPARENT,
            "#303030",
            "#3f3f46",
        ]
        self.begin_colors = [
            "#475569",
            "#047857",
            "#3f3f46",
            "#6d28d9",
            "#0f766e",
            "#0e7490",
            "#334155",
            "#7dd3fc",
        ]
        self.end_colors = [
            "#0f172a",
            "#064e3b",
            "#18181b",
            "#581c87",
            "#134e4a",
            "#164e63",
            "#0f172a",
            "#0c4a6e",
        ]
        self.book_details = book_details
        # print(the_book.id)
        # print(len(self.the_books))

    # Entry form function
    # def build(self):
        # Set three variables as the entry form text fields
        self.the_title = CopyInfoField(
            title=f"{self.book_details.book_details_lite.title}",
        )
        self.full_title = CopyInfoField(
            title=f"{self.book_details.book_details_lite.title} by {self.book_details.book_details_lite.authors_f}",
        )
        self.isbn13 = CopyInfoField(
            title=self.book_details.isbn13
        )
        self.specific_desc = CopyInfoField(
            title=f"[align=center][quote][i]Author(s):[/i] {self.book_details.book_details_lite.authors_f} | "
            f"[i]Publication:[/i] [b]{self.book_details.publisher}[/b] | "
            f"[i]Pages:[/i] [b]{self.book_details.page_count}[/b] | "
            f"[i]Date:[/i] [b]{self.book_details.book_details_lite.published_date}[/b][/quote][/align]",
            no_wrap=False,
            max_lines=2,
        )
        # self.filtered_desc = self.book_details.description
        html_to_text = html2text.HTML2Text()
        html_to_text.ignore_emphasis = True
        html_to_text.strong_mark = ""
        self.final_desc = html_to_text.handle(self.book_details.description)
        self.general_desc = CopyInfoField(
            title=f"[align=center][b][u]About the E-Book[/u][/b][/align]\n{self.final_desc}",
            no_wrap=False,
            max_lines=4,
        )

        self.host_image = ImageUploadField()

        # We need to seperate functions to open and close the dialog
        self.EntryForm = AlertDialog(
            # open=True,
            title=Container(
                # height=320,
                # width=400,
                padding=padding.all(6),
                content=Row(
                    vertical_alignment="start",
                    controls=[
                        Container(
                            content=Image(
                                src=self.book_details.book_details_lite.thumbnail_link,
                                width=128,
                                # height=100,
                                fit=ImageFit.COVER,
                                border_radius=border_radius.all(16),
                            ),
                            alignment=alignment.top_center,
                        ),
                        Column(
                            alignment="start",
                            spacing=2,
                            controls=[
                                Text(
                                    f"{self.book_details.book_details_lite.title} by {self.book_details.book_details_lite.authors_f}",
                                    size=14,
                                    weight='w700',
                                    color='#d7ccc9',
                                    width=160,
                                    text_align="left",
                                    no_wrap=False,
                                ),
                                InfoContainer(
                                    title=self.book_details.publisher,
                                    size=10,
                                    weight='w600',
                                    color='#c2dee1',
                                    width=160,
                                    alignment=alignment.center_left
                                ),
                                InfoContainer(
                                    title=self.book_details.book_details_lite.published_date,
                                    size=10,
                                    weight='w600',
                                    color='#dcedc1',
                                    width=160,
                                    alignment=alignment.center_left,
                                ),
                            ]
                        ),
                    ],
                ),
            ),
            content=Column(
                [
                    self.the_title,
                    self.full_title,
                    self.isbn13,
                    self.specific_desc,
                    self.general_desc,
                    self.host_image,
                ],
                spacing=8,
                # height=420,
            ),
            actions=[
                # These actions fire when they are clicked.
                TextButton(
                    "Done",
                    on_click=self.CloseForm,
                ),
            ],
            actions_alignment="center",
            on_dismiss=None,
        )
        # return self.EntryForm

    def CloseForm(self, e):
        self.EntryForm.open = False
        self.update()

    def build(self):
        return self.EntryForm

    def OpenForm(self):
        self.EntryForm.open = True

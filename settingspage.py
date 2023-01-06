from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, NavigationBar,
    NavigationDestination, FloatingActionButton, Margin, TextStyle
)
from settings import MySettings
from modals import CounterField, APIKeyField


class SettingsPage(UserControl):
    def __init__(self):
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
        super().__init__()

    def RestoreValues(self):
        self.APIKeyField.RestoreValue()
        self.CounterField.RestoreValue()

    def ClearValues(self, e):
        self.APIKeyField.ClearValue()
        self.CounterField.ClearValue()

    def UpdateValues(self, e):
        MySettings.api_key = self.APIKeyField.GetValue()
        MySettings.default_result_count = self.CounterField.GetValue()

    def MainContainer(self):
        self.APIKeyField = APIKeyField(self.api_key)
        self.CounterField = CounterField(self.default_result_count)
        self.DisableIcon = IconButton(
            icon=icons.SAVE_OUTLINED,
            icon_size=16,
            disabled=False,
            on_click=self.UpdateValues,
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
                            Text("Settings"),
                            Container(
                                content=Row(
                                    alignment="end",
                                    spacing=0,
                                    controls=[
                                        self.DisableIcon,
                                        IconButton(
                                            icon=icons.UPDATE_OUTLINED,
                                            icon_size=16,
                                            on_click=self.ClearValues,
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    self.APIKeyField,
                    self.CounterField,
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

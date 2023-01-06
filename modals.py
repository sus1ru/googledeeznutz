import pyperclip
import os
import asyncio
from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, NavigationBar,
    NavigationDestination, FloatingActionButton, Margin, TextStyle, animation
)
from flet.transform import Scale
from settings import MySettings
from backengine import BackEngine
from typing import Union, Optional

OptNum = Union[None, int, float]


def GradientGenerator(begin_col, end_col):
    return LinearGradient(
        begin=alignment.bottom_left,
        end=alignment.top_right,
        colors=[
            begin_col,
            end_col,
        ],
    )


class CopyInfoField(UserControl):
    def __init__(
        self,
        title: str,
        max_lines: Optional[int] = None,
        size: OptNum = 14,
        weight: str = 'w400',
        color: str = colors.WHITE,
        width: OptNum = 320,
        alignment: Optional[Alignment] = None,
        no_wrap: bool = True,
    ):
        super().__init__()
        self.title = title
        self.size = size
        self.weight = weight
        self.color = color
        self.max_lines = max_lines
        self.width = width
        self.alignment = alignment
        self.no_wrap = no_wrap
        self.InfoText = Text(
            self.title,
            size=self.size,
            weight=self.weight,
            color=self.color,
            max_lines=self.max_lines,
            no_wrap=self.no_wrap,
        )

    def _animate(self, e):
        if e.control.bgcolor != "#33363d":
            e.control.bgcolor = "#33363d"
        else:
            e.control.bgcolor = "#23242c"

        e.control.update()

    def build(self):
        return Container(
            content=self.InfoText,
            width=self.width,
            alignment=self.alignment,
            clip_behavior="antiAlias",
            bgcolor="#23242c",
            border_radius=border_radius.all(12),
            padding=padding.all(8),
            on_click=lambda e: pyperclip.copy(self.title),
            on_hover=lambda e: self._animate(e),
        )


class InfoContainer(UserControl):
    def __init__(
        self,
        title: str,
        size: OptNum = 10,
        weight: str = 'w600',
        color: str = colors.WHITE,
        width: OptNum = None,
        alignment: Optional[Alignment] = None,
        no_wrap: bool = True,
    ):
        super().__init__()
        self.title = title
        self.size = size
        self.weight = weight
        self.color = color
        self.width = width
        self.alignment = alignment
        self.InfoText = Text(
            self.title,
            size=self.size,
            weight=self.weight,
            color=self.color,
            no_wrap=True,
        )

    def build(self):
        return Container(
            content=self.InfoText,
            width=self.width,
            alignment=self.alignment,
            clip_behavior="antiAlias",
        )


class CounterField(UserControl):
    def __init__(self, init_value):
        self.init_value = init_value
        super().__init__()

    def RestoreValue(self):
        self.counter_field.value = MySettings.default_result_count
        self.counter_field.update()

    def ClearValue(self):
        self.counter_field.value = ""
        self.counter_field.update()

    def GetValue(self):
        return self.counter_field.value

    def counter_engine(self, op=""):
        try:
            int_val = int(self.counter_field.value)
        except:
            int_val = 1

        if op is icons.ADD:
            int_val = int_val + 1
        elif op is icons.REMOVE:
            int_val = int_val - 1

        if int_val > 16:
            int_val = 16
        elif int_val < 1:
            int_val = 1

        self.counter_field.value = str(int_val)
        self.counter_field.update()

    def build(self):
        self.counter_field = TextField(
            value=self.init_value,
            text_align="center",
            height=30,
            width=100,
            # prefix_icon=icons.REMOVE,
            # suffix_icon=icons.ADD,
            prefix=IconButton(
                icon=icons.REMOVE,
                icon_size=14,
                on_click=lambda e: self.counter_engine(icons.REMOVE),
            ),
            suffix=IconButton(
                icon=icons.ADD,
                icon_size=14,
                on_click=lambda e: self.counter_engine(icons.ADD),
            ),
            text_style=TextStyle(size=14, weight="w300"),
            content_padding=padding.symmetric(3, 0),
            border_color=colors.TRANSPARENT,
            border_radius=border_radius.all(16),
            # keyboard_type="phone",
            on_blur=self.counter_engine,
            filled=True,
        )
        return self.counter_field


class ImageUploadField(UserControl):
    def __init__(self):
        super().__init__()

    def upload_func(self, e):
        path = self.img_path_field.value
        if path != "":
            img_link = asyncio.run(
                BackEngine().img_up([os.path.abspath(path)]))
        self.img_path_field.value = img_link

        self.update()

    def build(self):
        self.img_path_field = TextField(
            value="",
            hint_text="Path to the image file...",
            height=36,
            # width=100,
            prefix=IconButton(
                icon=icons.UPLOAD,
                icon_size=14,
                on_click=self.upload_func,
            ),
            suffix=IconButton(
                icon=icons.COPY,
                icon_size=14,
                on_click=lambda e: pyperclip.copy(self.img_path_field.value),
            ),
            text_align="start",
            text_style=TextStyle(size=14, weight="w300"),
            content_padding=padding.only(0, 8, 0, 8),
            border_color=colors.TRANSPARENT,
            border_radius=border_radius.all(12),
            # keyboard_type="phone",
            filled=True,
        )
        return self.img_path_field


class APIKeyField(UserControl):
    def __init__(self, init_value):
        self.init_value = init_value
        super().__init__()

    def RestoreValue(self):
        self.api_key_field.value = MySettings.api_key
        self.api_key_field.update()

    def ClearValue(self):
        self.api_key_field.value = ""
        self.api_key_field.update()

    def GetValue(self):
        return self.api_key_field.value

    def build(self):
        self.api_key_field = self.APIKeyField = TextField(
            value=self.init_value,
            height=30,
            prefix_icon=icons.KEY,
            text_style=TextStyle(size=14, weight="w300"),
            content_padding=padding.only(0, 3, 12, 3),
            border_color=colors.TRANSPARENT,
            border_radius=border_radius.all(16),
            filled=True,
        )
        return self.api_key_field


class CustomButton(UserControl):
    ActivePage = "home"

    def __init__(self, icon_image, label, page_dict):
        self.icon_image = icon_image
        self.label = label
        self.page_dict = page_dict
        self.page_dict[self.label].visible = False
        self.my_colors = [
            colors.TRANSPARENT,
            "#303030",
            "#3f3f46",
        ]
        # print(the_book.id)
        # print(len(self.the_books))
        super().__init__()

    def page_visibility(self, e):
        if CustomButton.ActivePage == self.label:
            return

        CustomButton.ActivePage = self.label
        for key in self.page_dict.keys():
            self.page_dict[key].visible = False

        self.page_dict[CustomButton.ActivePage].visible = True

        if self.label == 'settings':
            self.page_dict[self.label].RestoreValues()

        e.page.update()

    def _animate(self, e):
        if e.control.content.color != colors.DEEP_ORANGE_200:
            e.control.content.color = colors.DEEP_ORANGE_200
        else:
            e.control.content.color = colors.WHITE

        if e.control.scale != 1.125:
            e.control.scale = 1.125
        else:
            e.control.scale = 1

        e.control.update()

    def build(self):
        return Card(
            elevation=8,
            margin=margin.only(10, 10, 4, 10),
            content=Container(
                width=48,
                height=48,
                # bgcolor=colors.DEEP_PURPLE,
                alignment=alignment.center,
                border_radius=border_radius.all(12),
                gradient=LinearGradient(
                    begin=alignment.bottom_left,
                    end=alignment.top_right,
                    colors=["#3f3f46", "#303030"],
                ),
                content=Icon(
                    name=self.icon_image,
                    color=colors.WHITE,
                    size=24,
                ),
                scale=Scale(scale=1),
                animate_scale=animation.Animation(1200, "bounceOut"),
                on_hover=lambda e: self._animate(e),
                on_click=self.page_visibility,
            ),
        )

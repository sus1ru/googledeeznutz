from homepage import HomePage
from settingspage import SettingsPage
import flet
from modals import CustomButton
from bookdetails import BookDetails
from flet import (
    UserControl, ListView, View, Text, colors, Card, Container, Alignment, alignment,
    Page, Column, Dropdown, dropdown, SnackBar, AlertDialog, Row, Icon, icons, AppBar,
    FontWeight, ElevatedButton, IconButton, padding, TextField, border, margin, Stack,
    ListTile, ProgressRing, GridView, border_radius, LinearGradient, NavigationBar,
    NavigationDestination, FloatingActionButton, Margin
)


# fl_json = open('vol2.json', "r")
# book_list = json.loads(fl_json.read())
# fl_json.close()


def main(page: Page):
    page.title = "Book2BBCodes"
    page.window_width = 420
    page.window_height = 744
    page.bgcolor = colors.TRANSPARENT
    page.padding = 0
    page.theme_mode = 'dark'

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # page.dialog = BookDetails()
    home = HomePage()
    settings = SettingsPage()
    # settings.visible = False
    page_dict = {
        home.label: home,
        settings.label: settings
    }
    home_tab = CustomButton(icons.HOME_OUTLINED, home.label, page_dict)
    profile_tab = CustomButton(icons.PERSON, settings.label, page_dict)

    BottomNavBar = Row(
        alignment="center",
        controls=[
            home_tab,
            profile_tab,
        ]
    )

    home.visible = True
    app = Stack(
        controls=[
            home,
            settings,
            Column(
                right=0,
                left=0,
                bottom=0,
                controls=[BottomNavBar],
            ),
        ]
    )
    page.add(app)
    # page.add(BottomNavBar)
    page.update()


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")

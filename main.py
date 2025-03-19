from cv2 import rotate
import math
import flet as ft
from flet import (
    ButtonStyle,
    Column,
    Container,
    Icon,
    IconButton,
    Page,
    RoundedRectangleBorder,
    Row,
    Text,
    Theme,
    WindowDragArea,
    padding,
)


class WindowControlButton(IconButton):
    def __init__(self, *args, icon_size: int, **kwargs):
        super().__init__(*args, icon_size=icon_size, **kwargs)
        self.height = 35
        self.width = 45
        self.style = ButtonStyle(
            shape=RoundedRectangleBorder(),
            color=ft.colors.ON_BACKGROUND,  # 小文字のスネークケースに変更
            overlay_color=ft.colors.SURFACE_VARIANT,  # 小文字のスネークケースに変更
        )


class WindowTitleBar(Container):
    ICON_SIZE = 15
    HEIGHT = 30

    def __init__(self, title: str, page: Page) -> None:
        super().__init__()
        self.page = page
        self.title = title

        # ボタンの初期化
        self.maximize_button = WindowControlButton(
            ft.icons.CROP_SQUARE_SHARP,
            icon_size=self.ICON_SIZE,
            rotate=math.pi,
            on_click=self.maximized_button_clicked,
        )
        self.minimize_button = WindowControlButton(
            ft.icons.MINIMIZE_SHARP,
            icon_size=self.ICON_SIZE,
            on_click=self.minimize_button_clicked,
        )
        self.close_button = WindowControlButton(
            ft.icons.CLOSE_SHARP,
            icon_size=self.ICON_SIZE,
            on_click=lambda _: self.page.window.close(),
        )

        self.content = Row(
            [
                WindowDragArea(
                    Row(
                        [
                            Container(
                                Icon(
                                    ft.icons.FAVORITE,
                                    color=ft.colors.SECONDARY,
                                    size=self.ICON_SIZE,
                                ),
                                padding=padding.only(5, 2, 0, 2),
                            ),
                            Text(
                                self.title,
                                color=ft.colors.SECONDARY,  # 小文字に変更
                            ),
                        ],
                        height=self.HEIGHT,
                    ),
                    expand=True,
                ),
                self.minimize_button,
                self.maximize_button,
                self.close_button,
            ],
            spacing=0,
        )
        self.bgcolor = ft.colors.PRIMARY_CONTAINER

    def minimize_button_clicked(self, e):
        self.page.window_minimized = True
        self.page.update()

    def maximized_button_clicked(self, e):
        self.page.window.maximized = True if not self.page.window.maximized else False
        self.page.update()

        if self.page.window.maximized:
            self.maximize_button.icon = ft.icons.FILTER_NONE
            self.maximize_button.icon_size = 12
        else:
            self.maximize_button.icon = ft.icons.CROP_SQUARE_SHARP
            self.maximize_button.icon_size = 15
        self.update()


class MainWindow(Container):
    def __init__(self, page: Page, window_title: str):
        super().__init__()
        page.window.frameless = True
        page.window_title_bar_hidden = True
        page.window_title_bar_buttons_hidden = True
        page.padding = 0  # これがないとタイトルバーが浮く

        page.theme_mode = "dark"
        page.theme = Theme(color_scheme_seed=ft.colors.BLUE_ACCENT)
        self.page = page
        self.title_bar = WindowTitleBar(window_title, self.page)
        self.content = Column(
            [
                self.title_bar,
                Content(),
            ],
            spacing=0,
        )
        self.bgcolor = ft.colors.BACKGROUND


class Content(Container):
    def __init__(self):
        super().__init__()
        self.content = Text(value="Content")
        self.padding = padding.all(10)


def main(page: Page):
    app = MainWindow(page, window_title="window Title")
    page.add(app)


if __name__ == "__main__":
    ft.app(main)

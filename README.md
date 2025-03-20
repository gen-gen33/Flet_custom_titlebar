# Flet Frameless Window and Custom Title Bar

This project demonstrates how to implement a frameless window with a custom title bar using Flet.

## Overview

- Uses Python 3.13.2 and Flet 0.27.6
- Replaces the system default title bar with a custom implementation
- Implements basic window functions: moving, minimizing, maximizing, and closing

## Key Code

### Frameless Window Configuration

```python
page.window.frameless = True
page.window_title_bar_hidden = True
page.window_title_bar_buttons_hidden = True
page.padding = 0  # Prevents the title bar from floating
```

### Custom Title Bar Implementation

```python
class WindowTitleBar(Container):
    def __init__(self, title: str, page: Page) -> None:
        # ...
        self.content = Row(
            [
                WindowDragArea(  # Window drag functionality
                    Row(
                        [
                            Container(Icon(ft.icons.FAVORITE)),
                            Text(self.title),
                        ],
                    ),
                    expand=True,
                ),
                self.minimize_button,  # Minimize button
                self.maximize_button,  # Maximize button
                self.close_button,     # Close button
            ],
        )
```

## Usage

```python
import flet as ft
from custom_titlebar import MainWindow

def main(page: ft.Page):
    app = MainWindow(page, window_title="Custom Title Bar Demo")
    page.add(app)

if __name__ == "__main__":
    ft.app(main)
```

## Customization

You can apply your own design by changing icons, colors, and styles.
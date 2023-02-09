from widget.menubar import MenuButtonType
from typing import List


def example(text)->str:
    return "This is an example."


buttons: List[MenuButtonType] = [
    {"name":"example", "behavior": example},
]
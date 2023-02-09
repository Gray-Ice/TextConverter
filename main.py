import sys
from typing import List
from widget.menubar import MenuButtonType
from PyQt5 import Qt as Q

from widget import MenuBar, TextViewer
from utils.buttons import buttons as custom_buttons
sys.path.append(".")


def plus_one(text: str):
    return text + "1"


class MainWidget(Q.QWidget):
    def __init__(self):
        super().__init__()
        self.editor = TextViewer(self)
        self.menubar = MenuBar(self)
        self._init_ui()

    def _init_ui(self):
        grid = Q.QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.menubar, 1, 0)
        grid.addWidget(self.editor, 2, 0)

    def load_buttons(self, buttons: List[MenuButtonType]):
        self.menubar.load_buttons_from_list(buttons)


if __name__ == "__main__":
    app = Q.QApplication(sys.argv)
    m = MainWidget()
    m.load_buttons(custom_buttons)
    m.show()
    sys.exit(app.exec_())

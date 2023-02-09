from PyQt5 import Qt as Q
from typing import TypedDict, List, Callable
from core import TextCore
from functools import partial


MenuButtonType = TypedDict("MenuButtonType", {
    "name": str,
    "behavior": Callable[[str], str]
})


class MenuBar(Q.QWidget):
    """
    功能按钮清单
    """
    def __init__(self, parent: Q.QWidget):
        super().__init__(parent)
        self.h_box = Q.QHBoxLayout(self)
        self.current_button_label = Q.QLabel(self)
        self._buttons = []
        self._init_ui()

    def _init_ui(self):
        #  添加控件
        self.current_button_label.setText("当前没有选择任何功能")
        self.setLayout(self.h_box)  # 设置布局
        self.h_box.addWidget(self.current_button_label)

    def load_buttons_from_list(self, buttons: List[MenuButtonType]):
        """
        从列表中加载Button。提供可定制性。
        :param buttons: List[MenuButtonType]。含有MenuButtonType类型的列表，本函数会用该列表初始化按钮栏的按钮。
        """
        for button in buttons:
            name = button['name']
            behavior = button['behavior']
            qbtn = Q.QPushButton(self)
            qbtn.setText(name)
            # 使用functools.partial()来达到C++中匿名函数的效果
            qbtn.clicked.connect(partial(self.on_button_clicked, name, behavior))
            self.h_box.addWidget(qbtn)


    def on_button_clicked(self, name: str, behavior: Callable):
        self.current_button_label.setText(name)
        TextCore.set_text_function(behavior)



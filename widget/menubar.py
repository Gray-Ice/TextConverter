from PyQt5 import Qt as Q
from typing import TypedDict, List, Callable
from core import TextCore
import core
from functools import partial
from utils.clipboard import get_clipboard
from text import MenuBar as MText, TextViewer


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
        self.change_mode_button = Q.QPushButton(self)
        self._trigger_on_clicked_text = MText.TRIGGER_ON_CLICKED
        self._set_function_on_clicked_text = MText.SET_FUNCTION_ON_CLICKED
        self._buttons = []
        self._init_ui()

    def _init_ui(self):
        #  添加控件
        self.current_button_label.setText(MText.DIDNOT_SET_BUTTON)
        if core.trigger_on_clicked:
            self.change_mode_button.setText(self._trigger_on_clicked_text)
        else:
            self.change_mode_button.setText(self._set_function_on_clicked_text)

        self.change_mode_button.clicked.connect(self._change_mode)
        self.setLayout(self.h_box)  # 设置布局
        self.h_box.addWidget(self.current_button_label)
        self.h_box.addWidget(self.change_mode_button)

    def _change_mode(self):
        """更改当前按钮的模式"""
        if core.trigger_on_clicked:
            core.trigger_on_clicked = not core.trigger_on_clicked
            self.change_mode_button.setText(self._set_function_on_clicked_text)
        else:
            core.trigger_on_clicked = not core.trigger_on_clicked
            self.change_mode_button.setText(self._trigger_on_clicked_text)
        print(core.trigger_on_clicked)

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
        # 设置显示当前处理函数Label和当前处理函数
        self.current_button_label.setText(name)
        TextCore.set_text_function(behavior)
        print(core.trigger_on_clicked)
        # 如果不是点击即触发模式，则设置已经完成，退出函数。
        if not core.trigger_on_clicked:
            return

        # 点击即触发功能模式
        text = get_clipboard()

        # 检测剪切板内容是否是文本
        if not text:
            self.parentWidget().editor.set_result_text_viewer(TextViewer.CLIPBOARD_ERROR)
            return

        # 开始执行功能
        result = TextCore.call_text_function(text)  # 调用当前设置的文本处理函数

        # 判断是否错误
        if result is False:
            self.parentWidget().editor.set_user_text_viewer(TextViewer.CLIPBOARD_ERROR)
            return
        if not isinstance(result, str):
            self.parentWidget().editor.set_result_text_viewer(TextViewer.CHOOSE_FUNCTION_RETURN_VALUE_ERROR)
            return

        # 设置结果文本框
        self.parentWidget().editor.set_result_text_viewer(result)

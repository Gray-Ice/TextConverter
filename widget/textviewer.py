from PyQt5 import Qt as Q
from core import TextCore
import win32clipboard
from typing import Union
from utils.clipboard import get_clipboard
from text import TextViewer as Text


class TextViewer(Q.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._user_text_viewer = _SubTextViewer(self)
        self._user_text_viewer.label.setText("输入(编辑不会有任何效果)")
        self._result_text_viewer = _SubTextViewer(self)
        self._result_text_viewer.label.setText("输出(编辑不会有任何效果)")
        self._button_row = _ButtonRow(self)
        self._init_ui()

    def _init_ui(self):
        h_box = Q.QHBoxLayout(self)  # 设置HBox布局
        #  添加控件
        h_box.addWidget(self._user_text_viewer)
        h_box.addWidget(self._button_row)
        h_box.addWidget(self._result_text_viewer)
        self.setLayout(h_box)  # 设置布局

    def set_result_text_viewer(self, string: str):
        self._result_text_viewer.editor.setText(string)

    def set_user_text_viewer(self, string: str):
        self._user_text_viewer.editor.setText(string)

    def get_result_text_viewer(self) -> str:
        return self._result_text_viewer.editor.toPlainText()

    def get_user_text_viewer(self) -> str:
        return self._user_text_viewer.editor.toPlainText()

    def enable_user_text_viewer(self) -> None:
        self._user_text_viewer.setEnabled(True)

    def disabled_user_text_viewer(self) -> None:
        self._user_text_viewer.setDisabled(True)

    def enable_result_text_viewer(self) -> None:
        self._result_text_viewer.setEnabled(True)

    def disabled_result_text_viewer(self) -> None:
        self._result_text_viewer.setDisabled(True)


class _SubTextViewer(Q.QWidget):
    """
    子类，结构为 VBox[label, 编辑器]。之所以声明该子类是为了在texteditor上方用label显示提示
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.editor = Q.QTextEdit(self)
        self.label = Q.QLabel(self)
        self._init_ui()

    def _init_ui(self):
        vlayout = Q.QVBoxLayout(self)
        self.setLayout(vlayout)
        vlayout.addWidget(self.label)
        vlayout.addWidget(self.editor)


class _ButtonRow(Q.QWidget):
    """编辑器按钮列表"""
    def __init__(self, parent):
        super().__init__(parent)
        self.copy_button = Q.QPushButton(self)
        self.paste_button = Q.QPushButton(self)
        self.paste_and_copy = Q.QPushButton(self)
        self._init_ui()
        # 连接槽函数
        self.paste_button.clicked.connect(self._paste_and_call_func)
        self.copy_button.clicked.connect(self._copy_result_text)
        self.paste_and_copy.clicked.connect(self._paste_and_copy_result)

    def _init_ui(self):
        vlayout = Q.QVBoxLayout(self)
        self.paste_button.setText("粘贴剪切板并处理")
        self.copy_button.setText("复制结果")
        self.paste_and_copy.setText("粘贴剪切板并复制结果")
        self.setLayout(vlayout)
        vlayout.addWidget(self.paste_button)
        vlayout.addWidget(self.copy_button)
        vlayout.addWidget(self.paste_and_copy)

    def _paste_and_call_func(self) -> None:
        """
        仅粘贴按钮的槽函数
        """
        text_viewer = self.parentWidget()
        text = get_clipboard()  # 判断是否获取剪切板成功
        if not text:
            text_viewer.set_result_text_viewer(Text.CLIPBOARD_ERROR)
            return

        result = TextCore.call_text_function(text)  # 调用当前设置的文本处理函数

        # 设置用户输入框
        text_viewer.set_user_text_viewer(text)
        # 非期望的输出
        if result is False:
            self.parentWidget().set_result_text_viewer(Text.DIDNOT_CHOOSE_FUNCTION)
            return
        if not isinstance(result, str):
            self.parentWidget().set_result_text_viewer(Text.CHOOSE_FUNCTION_RETURN_VALUE_ERROR)
            return

        self.parentWidget().set_result_text_viewer(result)

    def _copy_result_text(self) -> None:
        text = self.parentWidget().get_result_text_viewer()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
        return

    def _paste_and_copy_result(self) -> None:
        text_viewer = self.parentWidget()
        text = get_clipboard()  # 判断是否获取剪切板成功
        if not text:
            text_viewer.set_result_text_viewer(Text.CLIPBOARD_ERROR)
            return
        text_viewer.set_user_text_viewer(text)  # 设置用户输入文本

        result = TextCore.call_text_function(text)
        if result is False or not isinstance(result, str):
            self.parentWidget().set_result_text_viewer(Text.DIDNOT_CHOOSE_FUNCTION)
            return
        if not isinstance(result, str):
            self.parentWidget().set_result_text_viewer(Text.CHOOSE_FUNCTION_RETURN_VALUE_ERROR)
            return

        text_viewer.disable_result_text_viewer()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()
        self.parentWidget().set_result_text_viewer(result)
        text_viewer.enable_result_text_viewer()



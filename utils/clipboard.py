import win32clipboard
from typing import Union


def get_clipboard() -> Union[bool, str]:
    # 获取剪切板内容
    try:
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
    except TypeError:
        return False
    return text

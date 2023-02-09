from utils import SingletonClass
import win32clipboard


class TextCore(object):
    """文本处理核心类，单例。"""
    _text_function = None  # 文本处理方法，如果需要替换文本处理方法，需要调用set_text_function将本变量重新赋值即可。值应该为函数

    @classmethod
    def set_text_function(cls, func):
        """
        设置文本处理函数。程序同时只会使用一个文本处理函数
        :param func: Function(user_input: str) -> str。接收用户的输入，返回结果
        return: True
        """
        cls._text_function = func
        return True

    @classmethod
    def call_text_function(cls, text):
        """
        调用文本处理函数。文本处理函数类型应该是func(userinput: str) -> result: str
        :return: 当前文本处理函数返回的结果获False
        """

        if cls._text_function is None:  # 还没有设置文本处理函数
            return False
        result = cls._text_function(text)  # 调用文本处理函数
        if type(result) is not str:  # 文本处理函数返回值不是字符串
            return False

        return result

    @classmethod
    def class_text_function_and_paste_to_clipboard(cls, text):
        """
        自动将剪切板的内容传参给当前文本处理函数并且自动将处理结果发送到剪切板(clipboard)
        :return: 文本处理函数的处理结果或False
        """
        result = cls.call_text_function(text)
        if not result:
            return False

        if type(result) is not str:
            return False

        # 设置剪切板内容
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(result)
        win32clipboard.CloseClipboard()
        return result

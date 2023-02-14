class MenuBar(object):
    DIDNOT_SET_BUTTON = "当前没有选择任何功能"
    TRIGGER_ON_CLICKED = "切换为点击按钮设置状态"
    SET_FUNCTION_ON_CLICKED = "切换为点击按钮即触发"


class TextViewer(object):
    CLIPBOARD_ERROR = "获取剪切板错误！请检查当前复制内容是否为文本！"
    DIDNOT_CHOOSE_FUNCTION = "当前没有选择处理函数，或处理函数返回的结果不是一个字符串对象"
    CHOOSE_FUNCTION_RETURN_VALUE_ERROR = "处理函数返回的结果不是一个字符串对象"

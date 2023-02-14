from typing import TypedDict, Union, Any
from PyQt5 import Qt as Q
from utils import SingletonClass

# 全局组件管理类型。目的是提供主要组件类的访问方式
_WidgetManagerType = TypedDict("_WidgetManagerType", {
    "text_viewer": Union[None, Q.QWidget],
    "menu_bar": Union[None, Q.QWidget],
})

# 全局变量管理类型。目的是提供主要变量的访问方式
_VarManagerType = TypedDict("_VarManagerType", {
})

widget_manager: _WidgetManagerType = {"text_viewer": None, "menu_bar": None}

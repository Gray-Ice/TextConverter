from widget.menubar import MenuButtonType
from typing import List


def example(text)->str:
    return "This is an example."


def android_new_package_template(text: str) -> str:
    return "【此版本暂时未冒烟通过！！！各位慎重下载】\nAndroid\n" + text

def ios_new_package_template(text: str) -> str:
    return "【此版本暂时未冒烟通过！！！各位慎重下载】\nIOS\n" + text


# 在此处添加你定义的功能按钮，name是按钮的名称，behavior是点击按钮后会调用的函数，类型为(str)->str
buttons: List[MenuButtonType] = [
    {"name": "android", "behavior": android_new_package_template},
    {"name": "ios", "behavior": ios_new_package_template},
]
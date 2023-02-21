import io
import subprocess

from widget.menubar import MenuButtonType
from typing import List
import os
import sys

def example(text)->str:
    return "This is an example."


def android_new_package_template(text: str) -> str:
    return "【此版本暂时未冒烟通过！！！各位慎重下载】\nAndroid\n" + text

def ios_new_package_template(text: str) -> str:
    return "【此版本暂时未冒烟通过！！！各位慎重下载】\nIOS\n" + text


def run_install_ios(text: str) -> str:
    os.system(r"python C:\Users\v_szhewu\Desktop\Work\Tool\AutoInstallGNIpa.py")
    return "安装苹果安装包"

def run_install_android(text: str) -> str:
    os.system(r"python C:\Users\v_szhewu\Desktop\Work\Tool\AutoInstallGnyxAndApg.py")
    return "安装安卓安装包"


def get_push_info(text: str) -> str:
    sp = subprocess.Popen(args=["python", r"C:\Users\v_szhewu\Desktop\Work\Tool\GNQueryVersionCook1221.py"], shell=True, encoding="gb2312", stdout=subprocess.PIPE)
    out, err = sp.communicate()

    if err is None:
        return out.encode("utf-8").decode("utf-8")
    else:
        return err.encode("utf-8").decode("utf-8")


# 在此处添加你定义的功能按钮，name是按钮的名称，behavior是点击按钮后会调用的函数，类型为(str)->str
buttons: List[MenuButtonType] = [
    {"name": "android冒烟包消息", "behavior": android_new_package_template},
    {"name": "ios冒烟包消息", "behavior": ios_new_package_template},
    {"name": "安装苹果包", "behavior": run_install_ios},
    {"name": "安装苹果包", "behavior": run_install_android},
    {"name": "获取推送信息", "behavior": get_push_info},
]
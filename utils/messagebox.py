"""
该文件用于定义各类弹窗。
"""
from PyQt5 import Qt as _Q


def popup_error(error_msg: str):
    """
    弹窗展示error_msg。
    :param error_msg: 错误信息。该错误信息需要是字符串格式。
    :return: None
    """
    box = _Q.QMessageBox()
    box.setWindowTitle("Error")
    box.setText(error_msg)
    box.show()


def popup_info(info_msg: str):
    """
    弹窗展示info_msg。
    :param info_msg: 错误信息。该错误信息需要是字符串格式。
    :return: None
    """
    box = _Q.QMessageBox()
    box.setWindowTitle("Info")
    box.setText(info_msg)
    box.show()


def popup_warning(warning_msg: str):
    """
    弹窗展示warning_msg。
    :param warning_msg: 错误信息。该错误信息需要是字符串格式。
    :return: None
    """
    box = _Q.QMessageBox()
    box.setWindowTitle("Warning")
    box.setText(warning_msg)
    box.show()

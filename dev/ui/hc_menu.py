#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Anton Vanke <f@hpu.edu.cn>'

from PyQt5.Qt import *
from resource.hc_menu_ui import Ui_main_menu


class ModeSelection(QWidget, Ui_main_menu):
    # 返回主菜单信号
    return_mainmenu_singal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # 设置背景
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def return_main_menu(self):
        # 返回主菜单
        self.return_mainmenu_singal.emit()

    def about(self):
        # 关于菜单
        QMessageBox.about(self, "Python 五子棋",
                          "Github:<a href='https://github.com/AntonVanke/python-7days'>九宗七组</a> <br> Website:<a href='https://www.9z7.team/'>九宗七组</a>")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ModeSelection()
    window.show()
    sys.exit(app.exec_())

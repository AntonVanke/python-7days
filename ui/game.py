#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Anton Vanke <f@hpu.edu.cn>'

from PyQt5.Qt import *
from resource.game_ui import Ui_board


class GameBoard(QWidget, Ui_board):
    # 返回主菜单信号
    return_mainmenu_singal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # 设置背景

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def setupUi(self, board):
        super().setupUi(board)
        # 默认隐藏掉 背景音乐选项和音效选项
        self.music_checkbox.hide()
        self.sound_checkbox.hide()

    def return_main_menu(self):
        # 返回主菜单
        self.return_mainmenu_singal.emit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = GameBoard()
    window.show()
    sys.exit(app.exec_())

#!/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = 'Anton Vanke <f@hpu.edu.cn>'

import sys
from PyQt5.Qt import *

from main_menu import MainMenu
from game import GameBoard
from hc_menu import ModeSelection

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainmenu = MainMenu()


    def hc_menu():
        hc_choice = ModeSelection(mainmenu)
        hc_choice.show()
        hc_choice.return_mainmenu_singal.connect(hc_choice.hide)

    def human_computer_mode():
        # 人机对战模式
        hc_game = GameBoard(mainmenu)
        hc_game.show()
        hc_game.return_mainmenu_singal.connect(hc_game.hide)


    mainmenu.human_computer_mode_singal.connect(hc_menu)
    mainmenu.show()
    sys.exit(app.exec_())

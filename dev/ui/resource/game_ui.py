# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_board(object):
    def setupUi(self, board):
        board.setObjectName("board")
        board.resize(767, 767)
        board.setMinimumSize(QtCore.QSize(767, 767))
        board.setMaximumSize(QtCore.QSize(767, 767))
        board.setWindowOpacity(1.0)
        board.setStyleSheet("QWidget#board{\n"
"border-image: url(:/index/images/board.png);\n"
"}")
        self.setting_button = QtWidgets.QPushButton(board)
        self.setting_button.setEnabled(True)
        self.setting_button.setGeometry(QtCore.QRect(10, 720, 60, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setting_button.sizePolicy().hasHeightForWidth())
        self.setting_button.setSizePolicy(sizePolicy)
        self.setting_button.setMinimumSize(QtCore.QSize(0, 45))
        self.setting_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 0);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.setting_button.setCheckable(True)
        self.setting_button.setChecked(False)
        self.setting_button.setAutoDefault(False)
        self.setting_button.setObjectName("setting_button")
        self.return_mainmenu_button = QtWidgets.QPushButton(board)
        self.return_mainmenu_button.setEnabled(True)
        self.return_mainmenu_button.setGeometry(QtCore.QRect(634, 720, 121, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_mainmenu_button.sizePolicy().hasHeightForWidth())
        self.return_mainmenu_button.setSizePolicy(sizePolicy)
        self.return_mainmenu_button.setMinimumSize(QtCore.QSize(65, 45))
        self.return_mainmenu_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 0);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 128);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.return_mainmenu_button.setObjectName("return_mainmenu_button")
        self.player_image = QtWidgets.QLabel(board)
        self.player_image.setGeometry(QtCore.QRect(400, 0, 41, 51))
        self.player_image.setStyleSheet("background-image: url(:/index/images/cur_black.png);")
        self.player_image.setText("")
        self.player_image.setObjectName("player_image")
        self.player_lable = QtWidgets.QLabel(board)
        self.player_lable.setGeometry(QtCore.QRect(300, 0, 101, 41))
        self.player_lable.setStyleSheet("font: 16pt \"方正舒体\";")
        self.player_lable.setObjectName("player_lable")
        self.widget = QtWidgets.QWidget(board)
        self.widget.setGeometry(QtCore.QRect(280, 290, 202, 137))
        self.widget.setObjectName("widget")
        self.setting_menu = QtWidgets.QVBoxLayout(self.widget)
        self.setting_menu.setContentsMargins(0, 0, 0, 0)
        self.setting_menu.setSpacing(25)
        self.setting_menu.setObjectName("setting_menu")
        self.music_checkbox = QtWidgets.QCheckBox(self.widget)
        self.music_checkbox.setEnabled(True)
        self.music_checkbox.setMinimumSize(QtCore.QSize(200, 55))
        self.music_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.music_checkbox.setAutoFillBackground(False)
        self.music_checkbox.setStyleSheet("QCheckBox{\n"
"    font: 16pt \"方正舒体\";\n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 60px; height: 30px; \n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    background:url(:/index/images/switch_false_small.png)\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    background:url(:/index/images/switch_true_small.png)\n"
"}")
        self.music_checkbox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.music_checkbox.setCheckable(True)
        self.music_checkbox.setChecked(True)
        self.music_checkbox.setAutoRepeat(False)
        self.music_checkbox.setTristate(False)
        self.music_checkbox.setObjectName("music_checkbox")
        self.setting_menu.addWidget(self.music_checkbox)
        self.sound_checkbox = QtWidgets.QCheckBox(self.widget)
        self.sound_checkbox.setEnabled(True)
        self.sound_checkbox.setMinimumSize(QtCore.QSize(200, 55))
        self.sound_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sound_checkbox.setAutoFillBackground(False)
        self.sound_checkbox.setStyleSheet("QCheckBox{\n"
"    font: 16pt \"方正舒体\";\n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 60px; height: 30px; \n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    background:url(:/index/images/switch_false_small.png)\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    background:url(:/index/images/switch_true_small.png)\n"
"}")
        self.sound_checkbox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.sound_checkbox.setChecked(True)
        self.sound_checkbox.setAutoRepeat(False)
        self.sound_checkbox.setTristate(False)
        self.sound_checkbox.setObjectName("sound_checkbox")
        self.setting_menu.addWidget(self.sound_checkbox)

        self.retranslateUi(board)
        self.return_mainmenu_button.clicked.connect(board.return_main_menu)
        self.setting_button.clicked['bool'].connect(self.music_checkbox.setVisible)
        self.setting_button.clicked['bool'].connect(self.sound_checkbox.setVisible)
        QtCore.QMetaObject.connectSlotsByName(board)

    def retranslateUi(self, board):
        _translate = QtCore.QCoreApplication.translate
        board.setWindowTitle(_translate("board", "Python五子棋"))
        self.setting_button.setText(_translate("board", "设置"))
        self.return_mainmenu_button.setText(_translate("board", "返回主菜单"))
        self.player_lable.setText(_translate("board", "执子："))
        self.music_checkbox.setText(_translate("board", "背景音乐"))
        self.sound_checkbox.setText(_translate("board", "点击音效"))
import index_rc

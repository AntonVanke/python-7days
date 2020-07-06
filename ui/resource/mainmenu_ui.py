# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainmenu_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_menu(object):
    def setupUi(self, main_menu):
        main_menu.setObjectName("main_menu")
        main_menu.resize(767, 767)
        main_menu.setMinimumSize(QtCore.QSize(766, 767))
        main_menu.setMaximumSize(QtCore.QSize(767, 767))
        main_menu.setStyleSheet("QWidget#main_menu{\n"
"border-image: url(:/index/images/board.png);\n"
"}")
        self.about_button = QtWidgets.QPushButton(main_menu)
        self.about_button.setEnabled(True)
        self.about_button.setGeometry(QtCore.QRect(690, 720, 65, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_button.sizePolicy().hasHeightForWidth())
        self.about_button.setSizePolicy(sizePolicy)
        self.about_button.setMinimumSize(QtCore.QSize(65, 45))
        self.about_button.setStyleSheet("QPushButton{\n"
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
        self.about_button.setObjectName("about_button")
        self.setting_button = QtWidgets.QPushButton(main_menu)
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
        self.setting_button.setObjectName("setting_button")
        self.layoutWidget = QtWidgets.QWidget(main_menu)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 220, 191, 509))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(35)
        self.formLayout.setObjectName("formLayout")
        self.human_computer_mode_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.human_computer_mode_button.sizePolicy().hasHeightForWidth())
        self.human_computer_mode_button.setSizePolicy(sizePolicy)
        self.human_computer_mode_button.setMinimumSize(QtCore.QSize(0, 55))
        self.human_computer_mode_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 228);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.human_computer_mode_button.setObjectName("human_computer_mode_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.human_computer_mode_button)
        self.two_player_mode_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.two_player_mode_button.sizePolicy().hasHeightForWidth())
        self.two_player_mode_button.setSizePolicy(sizePolicy)
        self.two_player_mode_button.setMinimumSize(QtCore.QSize(0, 55))
        self.two_player_mode_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 228);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.two_player_mode_button.setObjectName("two_player_mode_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.two_player_mode_button)
        self.online_mode_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.online_mode_button.sizePolicy().hasHeightForWidth())
        self.online_mode_button.setSizePolicy(sizePolicy)
        self.online_mode_button.setMinimumSize(QtCore.QSize(0, 55))
        self.online_mode_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 228);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.online_mode_button.setObjectName("online_mode_button")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.online_mode_button)
        self.quit_game_button = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quit_game_button.sizePolicy().hasHeightForWidth())
        self.quit_game_button.setSizePolicy(sizePolicy)
        self.quit_game_button.setMinimumSize(QtCore.QSize(0, 55))
        self.quit_game_button.setStyleSheet("QPushButton{\n"
"    font: 14pt \"方正舒体\";\n"
"    \n"
"    \n"
"    background-color: rgba(169, 226, 223, 228);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(172, 206, 228, 228);\n"
"}\n"
"QPushButton:pressed{\n"
"    \n"
"    background-color: rgba(176, 184, 230, 228);\n"
"}")
        self.quit_game_button.setObjectName("quit_game_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.quit_game_button)
        self.layoutWidget.raise_()
        self.setting_button.raise_()
        self.about_button.raise_()

        self.retranslateUi(main_menu)
        self.about_button.clicked.connect(main_menu.about)
        self.quit_game_button.clicked.connect(main_menu.game_exit)
        self.human_computer_mode_button.clicked.connect(main_menu.human_computer_mode)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Python五子棋"))
        self.about_button.setText(_translate("main_menu", "关于"))
        self.setting_button.setText(_translate("main_menu", "设置"))
        self.human_computer_mode_button.setText(_translate("main_menu", "人机对战"))
        self.two_player_mode_button.setText(_translate("main_menu", "双人模式"))
        self.online_mode_button.setText(_translate("main_menu", "联机模式"))
        self.quit_game_button.setText(_translate("main_menu", "退出游戏"))
import index_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hc_menu_ui.ui'
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
        self.layoutWidget.setGeometry(QtCore.QRect(290, 270, 191, 235))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setVerticalSpacing(34)
        self.formLayout_2.setObjectName("formLayout_2")
        self.hc_computer = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hc_computer.sizePolicy().hasHeightForWidth())
        self.hc_computer.setSizePolicy(sizePolicy)
        self.hc_computer.setMinimumSize(QtCore.QSize(0, 55))
        self.hc_computer.setStyleSheet("QPushButton{\n"
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
        self.hc_computer.setObjectName("hc_computer")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.hc_computer)
        self.hc_humain = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hc_humain.sizePolicy().hasHeightForWidth())
        self.hc_humain.setSizePolicy(sizePolicy)
        self.hc_humain.setMinimumSize(QtCore.QSize(0, 55))
        self.hc_humain.setStyleSheet("QPushButton{\n"
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
        self.hc_humain.setObjectName("hc_humain")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.hc_humain)
        self.hc_computer_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hc_computer_2.sizePolicy().hasHeightForWidth())
        self.hc_computer_2.setSizePolicy(sizePolicy)
        self.hc_computer_2.setMinimumSize(QtCore.QSize(0, 55))
        self.hc_computer_2.setStyleSheet("QPushButton{\n"
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
        self.hc_computer_2.setObjectName("hc_computer_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.hc_computer_2)
        self.setting_button.raise_()
        self.about_button.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(main_menu)
        self.about_button.clicked.connect(main_menu.about)
        self.hc_computer_2.clicked.connect(main_menu.return_main_menu)
        QtCore.QMetaObject.connectSlotsByName(main_menu)

    def retranslateUi(self, main_menu):
        _translate = QtCore.QCoreApplication.translate
        main_menu.setWindowTitle(_translate("main_menu", "Python五子棋"))
        self.about_button.setText(_translate("main_menu", "关于"))
        self.setting_button.setText(_translate("main_menu", "设置"))
        self.hc_computer.setText(_translate("main_menu", "对方先手"))
        self.hc_humain.setText(_translate("main_menu", "我方先手"))
        self.hc_computer_2.setText(_translate("main_menu", "返回主菜单"))
import index_rc

from PyQt5.Qt import *
from resource.mainmenu_ui import Ui_main_menu


class MainMenu(QWidget, Ui_main_menu):
    # 人机对战信号
    human_computer_mode_singal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    def human_computer_mode(self):
        # 人机对战模式
        self.human_computer_mode_singal.emit()

    def about(self):
        # 关于菜单
        QMessageBox.about(self, "Python 五子棋",
                          "Github:<a href='https://github.com/AntonVanke/python-7days'>九宗七组</a> <br> Website:<a href='https://www.9z7.team/'>九宗七组</a>")

    def game_exit(self):
        # 游戏退出
        QCoreApplication.quit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())

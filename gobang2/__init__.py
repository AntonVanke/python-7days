#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
__version__ = "0.2.2"
__author__ = 'Anton Vanke <f@hpu.edu.cn>'


class Gobang:
    """
    五子棋
    =====
    一个简单的五子棋类, 可以在控制台下五子棋. 提供以下函数 :

        new(): 新局
        printcb(): 打印棋盘
        player(): 获取当前应落子 ID （轮走方）
        sortstep(): 处理总步表
        loadstep(): 将 step 步表的内容载入棋盘
        recall(): 前进后退的操作
        move(): 落子
        iswin(): 判断是否获胜
    """
    # 棋盘的边长
    SIDE = 15

    def new(self):
        """新局"""
        self.__init__()

    def printcb(self):
        """打印棋盘"""
        print("\033[7;32;40m+   ", end="")
        for c in range(65, 80):
            print(chr(c), end="   ")
        print("\033[0m\n")
        for row in range(len(self.chessboard)):
            print("\033[7;32;40m" + chr(row + 97), end="\033[0m   ")
            for i in self.chessboard[row]:
                if i == 0:
                    print(i, end="   ")
                elif i == 1:
                    print("\033[31m{}\033[0m".format(i), end="   ")
                elif i == 2:
                    print("\033[34m{}\033[0m".format(i), end="   ")
            print("\n")

    def player(self):
        """获取玩家ID"""
        return (len(self.step) % 2) + 1

    def sortstep(self):
        """将总步表分配给黑白子"""
        self.white, self.black = {}, {}
        for s in self.step.items():
            if s[0] % 2 == 1:
                self.black.update({s[0]: s[1]})
            else:
                self.white.update({s[0]: s[1]})

    def loadstep(self):
        """ 载入步表
        将 self.step 载入到棋盘上
        """
        try:
            self.chessboard = [[0 for i in range(self.SIDE)]
                               for j in range(self.SIDE)]
            step_list = list(self.step.values()).copy()
            for i in range(len(step_list)):
                self.chessboard[ord(step_list[i][0]) -
                                97][ord(step_list[i][1]) - 97] = (i % 2) + 1
            self.sortstep()
            return True
        except TypeError:
            return False

    def recall(self, s=-1):
        """ 悔棋
        """
        if s == -1:
            try:
                if len(self.max_step) < len(self.step):
                    self.max_step = self.step.copy()
                if len(self.step) == 0:
                    raise KeyError
            except KeyError:
                return False
            else:
                self.step.popitem()
                return self.loadstep()
        # 重下
        elif s == 1:
            if len(self.max_step) > len(self.step):
                self.step.update(
                    {len(self.step) + 1: self.max_step[len(self.step) + 1]})
                return self.loadstep()
            else:
                return False

    def move(self, row: int = 7, column: int = 7, **kwgs):
        """移動棋盘
        row: 棋盘的行号
        column: 棋盘的列号
        """
        if 's' in kwgs:
            row = ord(kwgs['s'][0].lower()) - 97
            column = ord(kwgs['s'][1].lower()) - 97
        # 判斷是否在棋盤上
        if 0 <= row < self.SIDE and 0 <= column < self.SIDE:
            # 判斷該位置上是否有子落過
            if self.chessboard[row][column] == 0:
                self.chessboard[row][column] = self.player()
                self.step[len(self.step) +
                          1] = chr(row + 97) + chr(column + 97)
                self.sortstep()
                return True
        return False

    def iswin(self):
        """判断是否结束
        """
        step_set_ls = []
        cb = self.chessboard
        # 将步表转换为列表
        for s in self.step.values():
            step_set_ls.append((ord(s[0]) - 97, ord(s[1]) - 97))
        # print(step_set_ls)
        for r, c in step_set_ls:
            try:
                # 判断 -- 行有 5 子
                if cb[r][c - 2] == cb[r][c - 1] == cb[r][c] == cb[r][
                    c + 1] == cb[r][c + 2] in (1, 2):
                    return True, cb[r][c]
            except IndexError:
                pass
            try:
                # 判断 | 有 5 子
                if cb[r - 2][c] == cb[r - 1][c] == cb[r][c] == cb[
                    r + 1][c] == cb[r + 2][c] in (1, 2):
                    return True, cb[r][c]
            except IndexError:
                pass
            try:
                # 判断 \ 有 5 子
                if cb[r - 2][c - 2] == cb[r - 1][c - 1] == cb[r][c] == cb[
                    r + 1][c + 1] == cb[r + 2][c + 2] in (1, 2):
                    return True, cb[r][c]
            except IndexError:
                pass
            try:
                # 判断 / 列有 5 子
                if cb[r + 2][c - 2] == cb[r + 1][c - 1] == cb[r][c] == cb[
                    r - 1][c + 1] == cb[r - 2][c + 2] in (1, 2):
                    return True, cb[r][c]
            except IndexError:
                pass
        return False, 0

    def __init__(self):
        # 棋盤
        self.chessboard = [[0 for i in range(self.SIDE)]
                           for j in range(self.SIDE)]
        # 總步表
        self.step = {}
        # 单局最长步表
        self.max_step = {}
        # 黑子步表
        self.black = {}
        # 白子步表
        self.white = {}


def _test():
    a = Gobang()
    # 输入步表
    a.step = {
        1: 'no',
        2: 'oo',
        3: 'mn',
        4: 'nn',
        5: 'lm',
        6: 'mm',
        7: 'kl',
        8: 'll',
    }
    # 加载
    a.loadstep()
    # 落子
    a.move(9, 10)
    # 打印棋盘
    a.printcb()
    # 输出输赢
    print(a.iswin())
    a.new()
    a.printcb()


if __name__ == "__main__":
    _test()

#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
__version__ = "0.2.2"
__author__ = 'Anton Vanke <f@hpu.edu.cn>'

import threading
import copy

states = [
    [1, 1, 1, 1, 1]  # 连五 - 99999
    , [0, 1, 1, 1, 1, 0]  # 活四 - 99998
    , [-1, 1, 1, 1, 1, 0]  # 冲四 1 - 50000
    , [0, 1, 1, 1, 1, -1]  # 冲四 1 - 50000
    , [1, 0, 1, 1, 1]  # 冲四 2 - 50000
    , [1, 1, 1, 0, 1]  # 冲四 2 - 50000
    , [1, 1, 0, 1, 1]  # 冲四 3 - 50000
    , [0, 1, 1, 1, 0, 0]  # 活三 1 - 10000
    , [0, 0, 1, 1, 1, 0]  # 活三 1 - 10000
    , [0, 1, 0, 1, 1, 0]  # 活三 2 - 10000
    , [0, 1, 1, 0, 1, 0]  # 活三 2 - 10000
    , [-1, 1, 1, 1, 0, 0]  # 眠三 1 - 5000
    , [0, 0, 1, 1, 1, -1]  # 眠三 1 - 5000
    , [-1, 1, 1, 0, 1, 0]  # 眠三 2 - 5000
    , [0, 1, 0, 1, 1, -1]  # 眠三 2 - 5000
    , [-1, 1, 0, 1, 1, 0]  # 眠三 3 - 5000
    , [0, 1, 1, 0, 1, -1]  # 眠三 3 - 5000
    , [1, 1, 0, 0, 1]  # 眠三 4 - 5000
    , [1, 0, 0, 1, 1]  # 眠三 4 - 5000
    , [1, 0, 1, 0, 1]  # 眠三 5 - 5000
    , [-1, 0, 1, 1, 1, -1]  # 眠三 6 - 5000
    , [0, 0, 1, 1, 0, 0]  # 活二 1 - 1000
    , [0, 1, 0, 1, 0, 0]  # 活二 2 - 1000
    , [0, 0, 1, 0, 1, 0]  # 活二 2 - 1000
    , [0, 1, 0, 0, 1, 0]  # 活二 3 - 1000
    , [-1, 1, 1, 0, 0, 0]  # 眠二 1 - 500
    , [0, 0, 0, 1, 1, -1]  # 眠二 1 - 500
    , [0, 1, 0, 1, 0, 0]  # 眠二 2 - 500
    , [0, 0, 1, 0, 1, 0]  # 眠二 2 - 500
    , [-1, 1, 0, 0, 1, 0]  # 眠二 3 - 500
    , [0, 1, 0, 0, 1, -1]  # 眠二 3 - 500
    , [1, 0, 0, 0, 1]  # 眠二 4 - 500
]

scores = [
    99999, 99998, 50000, 50000, 50000, 50000, 50000, 10000, 10000, 10000, 10000, 5000, 5000, 5000, 5000, 5000, 5000,
    5000, 5000, 5000, 5000, 1000, 1000, 1000, 1000, 500, 500, 500, 500, 500, 500, 500
]


class Ayer:
    """
    [1, 1, 1, 1, 1]  # 连五 - 99999
    [0, 1, 1, 1, 1, 0]  # 活四 - 99998
    [-1, 1, 1, 1, 1, 0]  # 冲四 1 - 50000
    [0, 1, 1, 1, 1, -1]  # 冲四 1 - 50000
    [1, 0, 1, 1, 1]  # 冲四 2 - 50000
    [1, 1, 1, 0, 1]  # 冲四 2 - 50000
    [1, 1, 0, 1, 1]  # 冲四 3 - 50000
    [0, 1, 1, 1, 0, 0]  # 活三 1 - 10000
    [0, 0, 1, 1, 1, 0]  # 活三 1 - 10000
    [0, 1, 0, 1, 1, 0]  # 活三 2 - 10000
    [0, 1, 1, 0, 1, 0]  # 活三 2 - 10000
    [-1, 1, 1, 1, 0, 0]  # 眠三 1 - 5000
    [0, 0, 1, 1, 1, -1]  # 眠三 1 - 5000
    [-1, 1, 1, 0, 1, 0]  # 眠三 2 - 5000
    [0, 1, 0, 1, 1, -1]  # 眠三 2 - 5000
    [-1, 1, 0, 1, 1, 0]  # 眠三 3 - 5000
    [0, 1, 1, 0, 1, -1]  # 眠三 3 - 5000
    [1, 1, 0, 0, 1]  # 眠三 4 - 5000
    [1, 0, 0, 1, 1]  # 眠三 4 - 5000
    [1, 0, 1, 0, 1]  # 眠三 5 - 5000
    [-1, 0, 1, 1, 1, -1]  # 眠三 6 - 5000
    [0, 0, 1, 1, 0, 0]  # 活二 1 - 1000
    [0, 1, 0, 1, 0, 0]  # 活二 2 - 1000
    [0, 0, 1, 0, 1, 0]  # 活二 2 - 1000
    [0, 1, 0, 0, 1, 0]  # 活二 3 - 1000
    [-1, 1, 1, 0, 0, 0]  # 眠二 1 - 500
    [0, 0, 0, 1, 1, -1]  # 眠二 1 - 500
    [0, 1, 0, 1, 0, 0]  # 眠二 2 - 500
    [0, 0, 1, 0, 1, 0]  # 眠二 2 - 500
    [-1, 1, 0, 0, 1, 0]  # 眠二 3 - 500
    [0, 1, 0, 0, 1, -1]  # 眠二 3 - 500
    [1, 0, 0, 0, 1]  # 眠二 4 - 500
    """
    _deepth = 5

    @classmethod
    def division(cls, board):
        # res 用来储存每个行列及斜线上的棋子
        res = []

        # 依次存入每行棋子
        for column in board:
            res.append(column)

        # 依次存入每列棋子
        for column in range(len(board)):
            row_line = []
            for row in range(len(board[column])):
                row_line.append(board[row][column])
            res.append(row_line)

        # 获取当 column >= row 时每个 \ 上的棋子
        for c in range(0, 11):
            oblique_1 = []
            for r in range(len(board) - c):
                oblique_1.append(board[r][c + r])
            res.append(oblique_1)

        # 获取当 column < row 时每个 \ 上的棋子
        for r in range(1, 11):
            oblique_2 = []
            for c in range(len(board) - r):
                oblique_2.append(board[r + c][c])
            res.append(oblique_2)

        # 获取当 column >= row 时每个 / 上的棋子
        for c in range(5, 15):
            oblique_3 = []
            for r in range(c + 1):
                oblique_3.append(board[r][c - r])
            res.append(oblique_3)

        # 获取当 column < row 时每个 / 上的棋子
        for r in range(1, 11):
            oblique_4 = []
            for c in range(14, r - 1, -1):
                oblique_4.append(board[r + len(board) - 1 - c][c])
            res.append(oblique_4)

        return res

    @classmethod
    def abp(cls, board, deepth, player):
        if deepth != 0:
            best_score = {}
            for r in range(len(board)):
                for c in range(len(board[r])):
                    board_temp = copy.deepcopy(board)
                    board_temp[r][c] = player
                    for state in states:
                        if player == 1:
                            if str(state)[1:-1] in str(cls.division(board_temp)).replace("], [", "]. [").replace("]",
                                                                                                                 "").replace(
                                "[", ""):
                                if scores[states.index(state)] > best_score.get(str([r, c]), 0):
                                    best_score[str([r, c])] = scores[states.index(state)]
                                    # best_score[str([r, c])] = cls.abp(board_temp, deepth-1, -player)
                        elif player == 2:
                            if str(state)[1:-1].replace("1", "2").replace("-1", "1") in str(
                                    cls.division(board_temp)).replace("], [", "]. [").replace("]", "").replace("[", ""):
                                if -scores[states.index(state)] < best_score.get(str([r, c]), 0):
                                    best_score[str([r, c])] = -scores[states.index(state)]
            return best_score

    def render(self):
        for r in self.chessboard:
            print(r)

    def __init__(self, step: dict, side=15):
        self.SIDE = side
        self.step = step
        self.chessboard = [[0 for i in range(self.SIDE)]
                           for j in range(self.SIDE)]
        step_list = list(self.step.values()).copy()
        for i in range(len(step_list)):
            self.chessboard[ord(step_list[i][0]) -
                            97][ord(step_list[i][1]) - 97] = (i % 2) + 1

            
            
if __name__ == '__main__':
    a = Ayer({1: 'hg', 2: 'ih', 3: 'lk', 4: 'il', 5: 'fk', 6: 'ei', 7: 'fh', 8: 'bj', 9: 'bm', 10: 'en', 11: 'hn', 12: 'in',
          13: 'ln', 14: 'mm', 15: 'mj', 16: 'lh', 17: 'gc', 18: 'fd', 19: 'ed', 20: 'je', 21: 'kl', 22: 'cf', 23: 'ni',
          24: 'lc', 25: 'hb', 26: 'cc', 27: 'bh', 28: 'dm', 29: 'dj', 30: 'dg', 31: 'ef', 32: 'ff', 33: 'bd', 34: 'df',
          35: 'eg', 36: 'eh', 37: 'dh', 38: 'di', 39: 'ci', 40: 'cj', 41: 'dl', 42: 'el', 43: 'fm', 44: 'hl', 45: 'hj',
          46: 'gi'})
    a.render()
    print(a.abp(a.chessboard, 1, 2))
print(a.division(a.chessboard))

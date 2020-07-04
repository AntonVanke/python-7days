import numpy as np


class Chess():
    """Gobang
    ==========
    基于Numpy的简单功能五子棋
    ==========
    功能
        1.提供一个15*15的棋盘基于Numpy
        2.提供在棋盘上的各种操作

    如何使用?
    -----------
    首先需要引用 `Chess` 像这样::
        >>> from gobang import Chess

    实例化一个玩家::
        >>> white = Chess('b') # `'b'` 代表子的颜色

    落子::
        >>> white.moveChessmen(7, 7) # `7, 7` 是落子位置

    悔棋::
        >>> white.regret()

    打印棋盘::
        >>> Chess.getCheckerboard()
        or::
        >>> white.getCheckerboard()

    获取步迹::
        >>> Chess.getStep() # 所有玩家步迹
        >>> white.getStep() # 此玩家步迹

    判断输赢::
        >>> white.isWin() # 返回 `True` 则white赢

    新局::
        >>> Chess.new()
        >>> white.new()

    其他
    -----
        >>> white.__dict__
        ...
    """

    # 棋盘形状(默认15*15)
    __checkerboard_shape = 15
    # 棋盘初始化
    __checkerboard = np.zeros((__checkerboard_shape, __checkerboard_shape),
                              dtype=int)
    # 玩家对应玩家ID
    __all_player_dict = {
        'black': 1,
        'white': 2,
        'Black': 1,
        'White': 2,
        'B': 1,
        'W': 2,
        'b': 1,
        'w': 2,
        '1': 1,
        '2': 2,
        1: 1,
        2: 2
    }

    # 玩家列表
    player_count = []
    # 步数统计
    step = {}

    # 新局
    def new(self=None):
        Chess.step = {}
        Chess.__checkerboard = np.zeros(
            (Chess.__checkerboard_shape, Chess.__checkerboard_shape),
            dtype=int)

    # 获取棋盘
    @classmethod
    def getCheckerboard(cls):
        """返回棋盘"""
        return Chess.__checkerboard

    # 获取落子
    def getStep(self=None):
        """Used to get step marks
        -----
        返回::
            如果使用 `Chess.getStep()`:
                返回所有的玩家步迹
            如果使用 `obj.getStep()`:
                返回此玩家步迹
        """
        if self is None:
            return Chess.step
        else:
            # 生成缓存步表
            step_ = {}

            for i in range(len(self.step)):
                # 寻找自身步数
                if i % 2 == self.__playerid - 1:
                    step_[i + 1] = self.step[i + 1]
            return step_

    # 判断是否获胜：仅提供五子棋的无禁手判断获胜方式
    def isWin(self, line_list=None):
        if line_list is None:
            line_list = self.arround()
        for line in line_list:
            if line[0].count(self.__playerid) >= 5:
                for i in range(0, len(line[0]) - 4):
                    if line[0][i] == line[0][i + 1] == line[0][i + 2] == line[
                            0][i + 3] == line[0][i + 4] == self.__playerid:
                        return True
        else:
            return False

    def arround(self=None, row=0, column=0):
        if self is not None:
            if len(self.getStep()) != 0:
                row = ord(list(self.getStep().items())[-1][1][0]) - 97
                column = ord(list(self.getStep().items())[-1][1][1]) - 97
            else:
                row = 7
                column = 7
        line_list, line_list1, line_list2, line_list3, line_list4 = [], [], [], [], []
        line_list1_, line_list2_, line_list3_, line_list4_ = [], [], [], []
        # 获取一整行
        line_list1 = [list(Chess.__checkerboard[row])]
        for i in range(len(Chess.__checkerboard[row])):
            line_list1_.append([row, i])
        line_list1.append(line_list1_)
        # 获取一整列
        line_list2 = [list(Chess.__checkerboard.T[column])]
        for i in range(len(Chess.__checkerboard.T[column])):
            line_list2_.append([i, column])
        line_list2.append(line_list2_)
        # 获取正斜线
        if row >= column:
            for i in range(14 - abs(row - column) + 1):
                line_list3.append(Chess.__checkerboard[i +
                                                       abs(row - column)][i])
            line_list3 = [line_list3]
            for i in range(14 - abs(row - column) + 1):
                line_list3_.append([i + abs(row - column), i])
            line_list3.append(line_list3_)
        if row < column:
            for i in range(14 - abs(row - column) + 1):
                line_list3.append(Chess.__checkerboard[i][i +
                                                          abs(row - column)])
            line_list3 = [line_list3]
            for i in range(14 - abs(row - column) + 1):
                line_list3_.append([i, i + abs(row - column)])
            line_list3.append(line_list3_)
        # 获取反斜线
        if row + column <= 14:
            for i in range(row + column + 1):
                line_list4.append(Chess.__checkerboard[i][row + column - i])
            line_list4 = [line_list4]
            for i in range(row + column + 1):
                line_list4_.append([i, row + column - i])
            line_list4.append(line_list4_)
        if row + column > 14:
            for i in range(28 - (row + column) + 1):
                line_list4.append(
                    Chess.__checkerboard[14 - i][14 - (28 -
                                                       (row + column) - i)])
            line_list4 = [line_list4]
            for i in range(28 - (row + column) + 1):
                line_list4_.append([14 - i, 14 - (28 - (row + column) - i)])
            line_list4.append(line_list4_)
        line_list.append(list(line_list1))
        line_list.append(list(line_list2))
        line_list.append(line_list3)
        line_list.append(line_list4)
        return line_list

    # 移动棋子
    def moveChessmen(self, row, column):
        # 判断行列合法性
        if row < self.__checkerboard_shape and column < self.__checkerboard_shape:
            # 判断当前位置是否落子
            if self.__checkerboard[row][column] == 0:
                # 判断落子顺序是否合法
                if len(self.step) % 2 == self.__playerid - 1:
                    self.row = row
                    self.column = column
                    # 给当前位置落子
                    self.__checkerboard[row][column] = self.__playerid
                    # 落子记录
                    self.step[len(self.step) +
                              1] = chr(row + 97) + chr(column + 97)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    # 悔棋
    def regret(self):
        self.row = ord(list(self.getStep().values())[-1][0]) - 97
        self.column = ord(list(self.getStep().values())[-1][1]) - 97
        if self.__can_regret:
            if len(self.step) % 2 == abs(self.__playerid -
                                         2) and len(self.step) != 0:
                self.__checkerboard[self.row][self.column] = 0
                self.step.pop(len(self.step))
                return True
            else:
                return False
        else:
            return False

    def isPlayer(self=None):
        if self is not None:
            if len(Chess.step) % 2 == self.__playerid - 1:
                return True
            else:
                return False
        else:
            if len(Chess.step) % 2 == 0:
                return "black"
            else:
                return "white"

    def __init__(self, player, player_name=None, can_regret=True):
        self.row = 0
        self.column = 0
        self.player_name = player_name
        self.__can_regret = can_regret

        # 判断玩家的重复、超出
        try:
            if len(self.player_count) < 2 and self.__all_player_dict[
                    player] not in self.player_count:
                # 赋予棋子ID
                self.__playerid = self.__all_player_dict[player]
                # 棋手加1
                self.player_count.append(self.__playerid)
            else:
                raise Exception("请检查玩家是否超出")
        except KeyError:
            raise KeyError("错误，请检查输入条件并查看文档")


def traversal_checkerboard():
    # 简单粗暴
    checkerboard = Chess.getCheckerboard()
    row_list, column_list = [], []
    row_list1, column_list1 = [], []
    for i in range(len(checkerboard)):
        row_list1 = [list(checkerboard[i])]
        row_list_ = []
        for j in range(len(checkerboard[i])):
            row_list_.append([i, j])
        # row_list.append([row_list_])
        row_list.append(row_list1 + [row_list_])
    # return row_list

    for i in range(len(checkerboard.T)):
        column_list1 = [list(checkerboard.T[i])]
        column_list_ = []
        for j in range(len(checkerboard.T[i])):
            column_list_.append([j, i])
        column_list.append(column_list1 + [column_list_])
    # return column_list

    slant = []
    for i in range(len(checkerboard)):
        slant.append(Chess.arround(row=i, column=0)[3])
    for i in range(1, len(checkerboard)):
        slant.append(Chess.arround(row=14, column=i)[3])
    # return slant

    b_slant = []
    for i in range(len(checkerboard)):
        b_slant.append(Chess.arround(row=i, column=0)[2])
    for i in range(1, len(checkerboard)):
        b_slant.append(Chess.arround(row=0, column=i)[2])
    # return b_slant
    # return row_list, column_list, slant, b_slant
    re_list = []
    re_list.append(row_list)
    re_list.append(column_list)
    re_list.append(slant)
    re_list.append(b_slant)
    return re_list


def aiChess():
    def get_score(id):
        score = [[1, [0, 0, 0, 0, id], [1, 2, 4, 6, 0]],
                 [1, [id, 0, 0, 0, 0], [0, 6, 4, 2, 1]],
                 [1, [0, 0, 0, id, 0], [2, 4, 6, 0, 1]],
                 [1, [0, id, 0, 0, 0], [1, 0, 6, 4, 2]],
                 [10, [0, 0, id, 0, 0], [1, 10, 0, 10, 1]],
                 [50, [0, id, id, 0, 0], [50, 0, 0, 50, 10]],
                 [50, [0, 0, id, id, 0], [10, 50, 0, 0, 50]],
                 [50, [0, id, 0, id, 0], [10, 0, 50, 0, 10]],
                 [200, [id, id, 0, id, 0], [0, 0, 200, 0, 50]],
                 [500, [0, 0, id, id, id], [50, 200, 0, 0, 0]],
                 [500, [id, id, id, 0, 0], [0, 0, 0, 200, 50]],
                 [5000, [0, id, id, id, 0], [200, 0, 0, 0, 200]],
                 [5000, [0, id, 0, id, id, 0], [200, 0, 500, 0, 0, 200]],
                 [5000, [0, id, id, 0, id, 0], [200, 0, 0, 500, 0, 200]],
                 [5000, [id, id, id, 0, id], [0, 0, 0, 500, 0]],
                 [5000, [id, id, 0, id, id], [0, 0, 500, 0, 0]],
                 [5000, [id, 0, id, id, id], [0, 50000, 0, 0, 0]],
                 [5000, [id, id, id, id, 0], [0, 0, 0, 0, 50000]],
                 [5000, [0, id, id, id, id], [50000, 0, 0, 0, 0]],
                 [99999999, [id, id, id, id, id], [0, 0, 0, 0, 0]]]
        return score

    def dict_span(dict1: dict, dict2: dict):
        weight = 100
        dict1_keys = list(dict1.keys())
        dict2_keys = list(dict2.keys())
        re_dict = {}
        for key in dict1_keys:
            if key in dict2_keys:
                re_dict[key] = (dict1[key] *
                                dict2[key]) / weight + dict2[key] + dict1[key]
            else:
                re_dict[key] = dict1[key]
        for key in dict2_keys:
            if key not in dict1_keys:
                re_dict[key] = dict2[key]

        return re_dict

    def get_p_score(id):
        p_score = {}
        for s_line in get_score(id):
            for _ in traversal_checkerboard():
                for i in _:
                    for j in range((len(i[0]) - len(s_line[1])) + 1):
                        if i[0][j:len(s_line[1]) + j] == s_line[1]:
                            for p in range(
                                    len(i[0][j + 1:len(s_line[1]) + j + 1])):
                                if str(i[0][j + 1:len(s_line[1]) + j +
                                            1][p]) in p_score:
                                    p_score[str(
                                        i[1][j:len(s_line[1]) + j]
                                        [p])] += s_line[0] * s_line[2][p]
                                else:
                                    p_score[str(
                                        i[1][j:len(s_line[1]) +
                                             j][p])] = s_line[0] * s_line[2][p]
        return p_score

    score = get_p_score(2)
    score_my = get_p_score(1)
    score = dict_span(score, score_my)
    if len(score) == 0:
        score = dict_span(score, score_my)

    return (eval(max(score, key=score.get))[0], eval(max(score,
                                                         key=score.get))[1])


def dicttoChees(step_dict):
    Chess.step = step_dict.copy()
    for r in range(len(Chess._Chess__checkerboard)):
        for c in range(len(Chess._Chess__checkerboard[r])):
            Chess._Chess__checkerboard[r][c] = 0
    if len(step_dict) != 0:
        for step in step_dict.items():
            row = ord(step[1][0]) - 97
            column = ord(step[1][1]) - 97
            if step[0] % 2 == 0:
                Chess._Chess__checkerboard[row][column] = 2
            elif step[0] % 2 == 1:
                Chess._Chess__checkerboard[row][column] = 1
    

def demo():
    a = Chess('B')
    b = Chess('W')
    a.moveChessmen(0, 4)
    b.moveChessmen(7, 14)
    a.moveChessmen(1, 3)
    b.moveChessmen(8, 13)
    a.moveChessmen(2, 2)
    b.moveChessmen(9, 12)
    a.moveChessmen(3, 1)
    b.moveChessmen(10, 11)
    a.moveChessmen(4, 0)
    b.moveChessmen(11, 10)
    # print(a.isWin())

    print(Chess.getCheckerboard())
    print(a.getStep())
    print(a.step)
    print(aiChess())


if __name__ == "__main__":
    demo()

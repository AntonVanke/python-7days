__version__ = "0.0.2"
__author__ = "9z7@9z7.team"

import copy


class Ayer:
    """

    ===============
    """
    # 有效区域, 定义有效区域可以减少搜索的范围, 默认的有效区域值为 2 : effarea()
    EA = 2
    SCORE = [[50, [0, 1, 1, 0, 0]],
             [50, [0, 0, 1, 1, 0]],
             [200, [1, 1, 0, 1, 0]],
             [500, [0, 0, 1, 1, 1]],
             [500, [1, 1, 1, 0, 0]],
             [5000, [0, 1, 1, 1, 0]],
             [5000, [0, 1, 0, 1, 1]],
             [5000, [0, 1, 1, 0, 1]],
             [5000, [1, 1, 1, 0, 1]],
             [5000, [1, 1, 0, 1, 1]],
             [5000, [1, 0, 1, 1, 1]],
             [5000, [1, 1, 1, 1, 0]],
             [5000, [0, 1, 1, 1, 1]],
             [50000, [0, 1, 1, 1, 1]],
             [99999999, [1, 1, 1, 1, 1]]]
    SCORE2 = [[50, [0, 2, 2, 0, 0]],
              [50, [0, 0, 2, 2, 0]],
              [200, [2, 2, 0, 2, 0]],
              [500, [0, 0, 2, 2, 2]],
              [500, [2, 2, 2, 0, 0]],
              [5000, [0, 2, 2, 2, 0]],
              [5000, [0, 2, 0, 2, 2]],
              [5000, [0, 2, 2, 0, 2]],
              [5000, [2, 2, 2, 0, 2]],
              [5000, [2, 2, 0, 2, 2]],
              [5000, [2, 0, 2, 2, 2]],
              [5000, [2, 2, 2, 2, 0]],
              [5000, [0, 2, 2, 2, 2]],
              [50000, [0, 2, 2, 2, 2]],
              [99999999, [2, 2, 2, 2, 2]]]

    def optimal(self):
        """最优选择器 FIXME: ……需要再调节一下
        """
        score = {"[7, 7]": 0}
        for r, c in self.effarea():
            if [r, c] not in self.step_set_ls:
                div = self.division(row=r, column=c, id=1)
                score_ = 0
                for d in div:
                    for s in self.SCORE:
                        if d[0] == s[1]:
                            if score_ < s[0]:
                                score_ = int(s[0])
                if str([r, c]) not in score.keys():
                    score[str([r, c])] = score_
                else:
                    score[str([r, c])] += score_
                div = self.division(row=r, column=c, id=2)
                score_ = 0
                for d in div:
                    for s in self.SCORE:
                        if d[0] == s[1]:
                            if score_ < s[0]:
                                score_ = int(s[0])
                if str([r, c]) not in score.keys():
                    score[str([r, c])] = score_
                else:
                    score[str([r, c])] += score_
        # 返回
        return eval(max(score, key=score.get))

    def printcb(self):
        # 打印棋盘 FIXME: 如果在 Jupyter 上显示就会乱码
        print("\033[7;32;40m+   ", end="")
        for c in range(65, 80):
            print(chr(c), end="   ")
        print("\033[0m\n")
        for row in range(len(self.cb)):
            print("\033[7;32;40m" + chr(row + 97), end="\033[0m   ")
            for column in range(len(self.cb[row])):
                if self.cb[row][column] == 0:
                    if [row, column] in self.area:
                        print("\033[34m{}\033[0m".format(0), end="   ")
                    else:
                        print(0, end="   ")
                else:
                    print("\033[31m{}\033[0m".format(self.cb[row][column]), end="   ")
            print("\n")

    def division(self, row=-1, column=-1, id=0):
        """分离 FIXME：分割时可以按 6 位来分割
        """
        cbc = copy.deepcopy(self.cb)
        if row != -1:
            cbc[row][column] = id
        section = []
        for r in range(2, self.SIDE - 2):
            for c in range(2, self.SIDE - 2):
                t = [[cbc[r][c - 2], cbc[r][c - 1], cbc[r][c], cbc[r][c + 1], cbc[r][c + 2]],
                     [[r, c - 2], [r, c - 1], [r, c], [r, c + 1], [r, c + 2]]]
                section.append(t)
                t = [[cbc[r - 2][c], cbc[r - 1][c], cbc[r][c], cbc[r + 1][c], cbc[r + 2][c]],
                     [[r - 2, c], [r - 1, c], [r, c], [r + 1, c], [r + 2, c]]]
                section.append(t)
                t = [[cbc[r - 2][c - 2], cbc[r - 1][c - 1], cbc[r][c], cbc[r + 1][c + 1], cbc[r + 2][c + 2]],
                     [[r - 2, c - 2], [r - 1, c - 1], [r, c], [r + 1, c + 1], [r + 2, c + 2]]]
                section.append(t)
                t = [[cbc[r + 2][c - 2], cbc[r + 1][c - 1], cbc[r][c], cbc[r - 1][c + 1], cbc[r - 2][c + 2]],
                     ([[r + 2, c - 2], [r + 1, c - 1], [r, c], [r - 1, c + 1], [r - 2, c + 2]])]
                section.append(t)
        return section

    def effarea(self):
        # 拷贝位置列表
        area_ = copy.deepcopy(self.step_set_ls)

        # 根据位置列表推导出有效区域列表
        for r, c in self.step_set_ls:
            for rr in range(r - self.EA, r + self.EA + 1):
                for cc in range(c - self.EA, c + self.EA + 1):
                    if 0 <= rr <= 14 and 0 <= cc <= 14:
                        area_.append([rr, cc])

        # 去重
        for e in area_:
            if e not in self.area:
                self.area.append(e)
        return self.area

    def __init__(self, step_dict: dict):
        # 定义棋盘边长
        self.SIDE = 15
        # 定义一个位置列表
        self.step_set_ls = []
        # 将输入的步表拷贝
        self.step = copy.deepcopy(step_dict)
        # 有效区域列表
        self.area = []

        # 将步表导入位置列表
        for s in self.step.values():
            self.step_set_ls.append([ord(s[0]) - 97, ord(s[1]) - 97])

        # 初始化棋盘
        chessboard = [[0 for i in range(self.SIDE)] for j in range(self.SIDE)]

        # 根据步表填充棋盘
        step_list = list(self.step.values()).copy()
        for i in range(len(step_list)):
            chessboard[ord(step_list[i][0]) - 97][ord(step_list[i][1]) - 97] = (i % 2) + 1
        self.cb = copy.deepcopy(chessboard)


def test():
    a = Ayer(
        {1: 'hg', 2: 'ih', 3: 'lk', 4: 'il', 5: 'fk', 6: 'ei', 7: 'fh', 8: 'bj', 9: 'bm', 10: 'en', 11: 'hn', 12: 'in',
         13: 'ln', 14: 'mm', 15: 'mj', 16: 'lh', 17: 'gc', 18: 'fd', 19: 'ed', 20: 'je', 21: 'kl', 22: 'cf', 23: 'ni',
         24: 'lc', 25: 'hb', 26: 'cc', 27: 'bh', 28: 'dm', 29: 'dj', 30: 'dg', 31: 'ef', 32: 'ff', 33: 'bd', 34: 'df',
         35: 'eg', 36: 'eh', 37: 'dh', 38: 'di', 39: 'ci', 40: 'cj', 41: 'dl', 42: 'el', 43: 'fm', 44: 'hl', 45: 'hj',
         46: 'gi'})
    a.printcb()

    import time

    start = time.time()
    if a.optimal() == [9, 12]:
        end = time.time()
        print('最优解匹配成功Running time : %s Seconds' % (end - start))


if __name__ == '__main__':
    test()

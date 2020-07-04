import os
import re
import time


import threading
import thread_stop

from gobang import Chess
from gobang import aiChess
from gobang import dicttoChees

import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
from PIL import ImageTk, Image

times = int(time.time())
# 加载资源文件夹
base_folder = os.path.dirname(__file__)
source_folder = os.path.join(base_folder, 'source')
img_folder = os.path.join(source_folder, 'img')
ex_folder = os.path.join(source_folder, 'ex')
root = tk.Tk()
# 设置标题
root.title("简单的python五子棋")
# 设置图标
root.iconphoto(False, tk.PhotoImage(file=os.path.join(img_folder, 'icon.png')))
# 定义宽高
WIDTH = 900
HEIGHT = 667
# 定义网格
LENGTH = 44
START = 22
# 窗口大小固定
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

# 选项配置
order_checkbutton_var = tk.IntVar()
order = False
putlist_checkbutton_var = tk.IntVar()
putlist = False
# 创建画布
canvas = tk.Canvas(root,
                   width=WIDTH,
                   height=HEIGHT,
                   bd=0,
                   highlightthickness=0)
# 设置背景颜色
background = ImageTk.PhotoImage(
    Image.open(os.path.join(img_folder, 'background_c.png')))

canvas.create_image(0, 0, anchor='nw', image=background)
canvas.pack()


# /////////////// #
#    主体开始      #
# /////////////// #


def game_exit():
    # 游戏退出
    if tkinter.messagebox.askyesno('退出游戏提示', '要退出游戏吗？'):
        os._exit(0)


def open_gs():
    # 打开棋谱文件 TODO
    gs_file = tkinter.filedialog.askopenfilename(title="选择棋谱",
                                                 initialdir=ex_folder,
                                                 filetypes=[("棋谱文件", ".sgf"),
                                                            ("棋谱文件", ".gbs"),
                                                            ("Gobang棋谱文件",
                                                             ".gbs")])
    if gs_file != '':
        try:
            with open(gs_file, encoding='utf-8') as f:
                gs_text = f.read()
        except UnicodeDecodeError:
            with open(gs_file) as f:
                gs_text = f.read()
        finally:
            step_dict = {}
            step_list = re.findall(r"[\[']([a-z][a-z])['\]]", gs_text)
            for i in range(len(step_list)):
                step_dict[i + 1] = step_list[i]
            score_mode(step_dict)


def save_gbs():
    # 保存棋谱文件 `gbs` 格式
    gbs_data = tkinter.filedialog.asksaveasfile(mode='w',
                                                title="选择棋谱",
                                                initialdir=ex_folder,
                                                defaultextension=".espace",
                                                filetypes=[("Gobang棋谱文件",
                                                            ".gbs")])
    if gbs_data is not None:
        gbs_data.write(str(Chess.getStep()))


def click(event):
    if not w.isWin() and not b.isWin():
        ismove_x = False
        ismove_y = False
        if 10 < event.x < 650 and 10 < event.y < 650:
            if (event.x - START) % LENGTH < 20:
                x = (event.x - START) // LENGTH
                ismove_x = True
            elif (event.x - START) % LENGTH > 24:
                x = ((event.x - START) // LENGTH) + 1
                ismove_x = True
            if (event.y - START) % LENGTH < 20:
                y = (event.y - START) // LENGTH
                ismove_y = True
            elif (event.y - START) % LENGTH > 24:
                y = ((event.y - START) // LENGTH) + 1
                ismove_y = True
            if ismove_x and ismove_y:
                move(y, x)


def move(y, x):
    # 落子
    global times
    if not w.isWin() and not b.isWin():
        if w.isPlayer():
            if w.moveChessmen(y, x):
                draw()
        elif b.isPlayer():
            if b.moveChessmen(y, x):
                draw()
    if w.isWin():
        tkinter.messagebox.showinfo('提示', '白方获胜！')
    if b.isWin():
        tkinter.messagebox.showinfo('提示', '黑方获胜！')



def draw(step_dict=None):
    # 绘制棋盘
    canvas.delete('Piece')
    color = {1: 'black', 0: 'white'}
    if step_dict is None:
        step_dict = Chess.getStep().copy()
    for step in step_dict.items():
        row = ord(step[1][0]) - 97
        column = ord(step[1][1]) - 97
        y1 = START + (LENGTH * row) - 20
        x1 = START + (LENGTH * column) - 20
        y2 = START + (LENGTH * row) + 20
        x2 = START + (LENGTH * column) + 20
        canvas.create_oval(x1,
                           y1,
                           x2,
                           y2,
                           fill=color[(step[0] % 2)],
                           tags='Piece')
        if step[0] == len(step_dict.items()):
            canvas.create_oval(x1 + 15,
                               y1 + 15,
                               x2 - 15,
                               y2 - 15,
                               fill='pink',
                               tags='Piece')
        if order:
            canvas.create_text(x1 + 20,
                               y1 + 20,
                               text=str(step[0]),
                               fill=color[int(not bool((step[0] % 2)))],
                               tags='Piece')
    # print(draw_list) # 测试输出


def regret():
    if len(Chess.step) != 0:
        if b.isPlayer():
            if w.regret():
                draw()
        elif w.isPlayer():
            if b.regret():
                draw()


def tips():
    # 提示
    if len(Chess.getStep().items()) == 0:
        b.moveChessmen(7, 7)
    # elif not M:
    else:
        rc = aiChess()
        move(rc[0], rc[1])
    draw()


def new():
    # 新局
    if tkinter.messagebox.askyesno('重新开始', '要重新开始游戏吗？'):
        Chess.new()
        draw()


def sign(event):
    # 获取鼠标实时位置，做出提示
    # time.sleep(0.08)
    canvas.delete("Sign")
    ismove_x = False
    ismove_y = False
    if 10 < event.x < 650 and 10 < event.y < 650 and not w.isWin(
    ) and not b.isWin():
        if (event.x - START) % LENGTH < 20:
            x = (event.x - START) // LENGTH
            ismove_x = True
        elif (event.x - START) % LENGTH > 24:
            x = ((event.x - START) // LENGTH) + 1
            ismove_x = True
        if (event.y - START) % LENGTH < 20:
            y = (event.y - START) // LENGTH
            ismove_y = True
        elif (event.y - START) % LENGTH > 24:
            y = ((event.y - START) // LENGTH) + 1
            ismove_y = True
        if ismove_x and ismove_y:
            y1 = START + (LENGTH * y) - 20
            x1 = START + (LENGTH * x) - 20
            y2 = START + (LENGTH * y) + 20
            x2 = START + (LENGTH * x) + 20
            canvas.create_oval(x1 + 15,
                               y1 + 15,
                               x2 - 15,
                               y2 - 15,
                               fill='red',
                               tags='Sign')


def show_order():
    # 是否显示落子序号
    global order
    order = bool(order_checkbutton_var.get())
    draw()


def show_putlist():
    # 输出日志信息
    global putlist
    putlist = bool(putlist_checkbutton_var.get())


def c_s():
    # 获取鼠标实时位置，做出提示
    canvas.bind("<Motion>", sign)
    # 落子
    canvas.bind("<ButtonRelease-1>", click)


def score_mode(step_dict):
    canvas.delete('ButtonScore')
    temp_dict = step_dict.copy()
    Chess.new()
    dicttoChees(step_dict)
    draw()

    def forward():
        # 下一步
        if len(temp_dict) != len(step_dict):
            temp_dict.update(
                {len(temp_dict) + 1: step_dict[len(temp_dict) + 1]})
            dicttoChees(temp_dict)
            draw()

    def retreat():
        # 上一步
        if len(temp_dict) != 0:
            temp_dict.popitem()
            dicttoChees(temp_dict)
            draw()

    def play():
        def stop():
            thread_stop.stop_thread(t)
            regret_button = tk.Button(root, text='⏩', command=play)
            canvas.create_window(767,
                                 370,
                                 anchor='nw',
                                 width=30,
                                 height=30,
                                 window=regret_button,
                                 tags='ScoreMode')

        regret_button = tk.Button(root, text='⏸', command=stop)
        canvas.create_window(767,
                             370,
                             anchor='nw',
                             width=30,
                             height=30,
                             window=regret_button,
                             tags='ScoreMode')
        nonlocal temp_dict
        if len(temp_dict) == len(step_dict):
            temp_dict = {}

        def play_t():
            for i in range(len(step_dict) - len(temp_dict)):
                forward()
                time.sleep(1)
            regret_button = tk.Button(root, text='⏩', command=play)
            canvas.create_window(767,
                                 370,
                                 anchor='nw',
                                 width=30,
                                 height=30,
                                 window=regret_button,
                                 tags='ScoreMode')

        t = threading.Thread(target=play_t)
        t.start()

    regret_button = tk.Button(root, text='◀', command=retreat)
    canvas.create_window(720,
                         370,
                         anchor='nw',
                         width=30,
                         height=30,
                         window=regret_button,
                         tags='ScoreMode')

    regret_button = tk.Button(root, text='⏩', command=play)
    canvas.create_window(767,
                         370,
                         anchor='nw',
                         width=30,
                         height=30,
                         window=regret_button,
                         tags='ScoreMode')

    regret_button = tk.Button(root, text='▶', command=forward)
    canvas.create_window(810,
                         370,
                         anchor='nw',
                         width=30,
                         height=30,
                         window=regret_button,
                         tags='ScoreMode')

    # 返回主菜单
    return_button = tk.Button(root, text='返回主菜单', command=button_main)
    canvas.create_window(720,
                         500,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=return_button,
                         tags='ButtonScore')


def Test__():
    # 保存测试
    canvas.delete('ButtonMain')


def button_score():
    # 初始化
    c_s()
    Chess.new()
    draw()
    canvas.delete('ButtonMain')
    # 新局
    open_gs_button = tk.Button(root, text='新局', command=new)
    canvas.create_window(720,
                         100,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=open_gs_button,
                         tags='ButtonScore')

    # 载入棋谱
    open_gs_button = tk.Button(root, text='载入棋谱', command=open_gs)
    canvas.create_window(720,
                         190,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=open_gs_button,
                         tags='ButtonScore')
    # 悔棋
    regret_button = tk.Button(root, text='悔棋', command=regret)
    canvas.create_window(720,
                         280,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=regret_button,
                         tags='ButtonScore')
    # 保存棋谱
    save_gbs_button = tk.Button(root, text='保存棋谱', command=save_gbs)
    canvas.create_window(720,
                         370,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=save_gbs_button,
                         tags='ButtonScore')
    # 返回主菜单
    return_button = tk.Button(root, text='返回主菜单', command=button_main)
    canvas.create_window(720,
                         500,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=return_button,
                         tags='ButtonScore')


def detector():
    while True:
        if len(w.getStep()) < len(b.getStep()) and not w.isWin() and not b.isWin():
            tips()


def button_m():
    # 人机对战菜单
    c_s()
    Chess.new()
    draw()
    global auto
    auto = threading.Thread(target=detector)
    auto.start()
    canvas.delete('ButtonMain')
    # 新局
    open_gs_button = tk.Button(root, text='新局', command=new)
    canvas.create_window(720,
                         100,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=open_gs_button,
                         tags='ButtonM')
    # 悔棋
    regret_button = tk.Button(root, text='悔棋', command=regret)
    canvas.create_window(720,
                         190,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=regret_button,
                         tags='ButtonM')
    # 提示
    tips_button = tk.Button(root, text='提示', command=tips)
    canvas.create_window(720,
                         280,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=tips_button,
                         tags='ButtonM')

    # 保存棋谱
    save_gbs_button = tk.Button(root, text='保存棋谱', command=save_gbs)
    canvas.create_window(720,
                         370,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=save_gbs_button,
                         tags='ButtonM')
    # 返回主菜单
    return_button = tk.Button(root, text='返回主菜单', command=button_main)
    canvas.create_window(720,
                         460,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=return_button,
                         tags='ButtonM')


def button_main():
    # 主菜单函数
    canvas.delete('ButtonScore')
    canvas.delete('ButtonM')
    canvas.delete('ScoreMode')

    # 解绑事件
    canvas.unbind("<ButtonRelease-1>")
    canvas.unbind("<Motion>")
    try:
        thread_stop.stop_thread(auto)
    except:
        pass
    # 人机对战按钮
    man_machine_button = tk.Button(root, text='人机对战', command=button_m)
    canvas.create_window(720,
                         100,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=man_machine_button,
                         tags='ButtonMain')

    # 打谱模式按钮
    score_button = tk.Button(root, text='打谱模式', command=button_score)
    canvas.create_window(720,
                         190,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=score_button,
                         tags='ButtonMain')

    # 退出游戏按钮
    game_exit_button = tk.Button(root, text='退出游戏', command=game_exit)
    canvas.create_window(720,
                         280,
                         anchor='nw',
                         width=120,
                         height=50,
                         window=game_exit_button,
                         tags='ButtonMain')

    # 测试按钮
    # debug_button = tk.Button(root, text='测试按钮', command=Test__)
    # canvas.create_window(720,
    #                      460,
    #                      anchor='nw',
    #                      width=120,
    #                      height=50,
    #                      window=debug_button,
    #                      tags='ButtonMain')


b = Chess('b', player_name="Computer.Python.AI", can_regret=True)
w = Chess('w', player_name="Computer.Python.AI", can_regret=True)

order_checkbutton = tk.Checkbutton(root,
                                   text="显示序号",
                                   variable=order_checkbutton_var,
                                   onvalue=1,
                                   offvalue=0,
                                   height=5,
                                   width=20,
                                   command=show_order)
canvas.create_window(667,
                     617,
                     anchor='nw',
                     width=120,
                     height=50,
                     window=order_checkbutton,
                     tags='Checkbutton')

putlist_checkbutton = tk.Checkbutton(root,
                                     text="输出LOG",
                                     variable=putlist_checkbutton_var,
                                     onvalue=1,
                                     offvalue=0,
                                     height=5,
                                     width=20,
                                     command=show_putlist)
canvas.create_window(787,
                     617,
                     anchor='nw',
                     width=120,
                     height=50,
                     window=putlist_checkbutton,
                     tags='Checkbutton')

button_main()
# 关闭提示
root.protocol("WM_DELETE_WINDOW", game_exit)
root.mainloop()

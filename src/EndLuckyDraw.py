# -*- coding:utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import random
import Image
import Tkinter as tk
from PIL import Image, ImageTk
import tkMessageBox as tkm
import HomePage as hp
import AdjustPhoto as adjph

# ---------抽奖结束--------- #
class GUIEndLuckyDraw:

    # 初始化界面
    def __init__(self):
        # 初始化界面
        self.top = tk.Tk()
        curWidth = 800
        curHeight = 500
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()
        x = (sw - curWidth) / 2
        y = (sh - curHeight) / 2
        cursize = '%dx%d+%d+%d' % (curWidth, curHeight, x, y)
        self.top.geometry(cursize)
        self.top.title('方圆羽毛球俱乐部2019年庆')
        path = os.path.abspath('..')+'/Image/system/end.png'
        self.backim = tk.PhotoImage(file=path)
        tk.Label(self.top,
                 text='抽奖结束，谢谢大家',
                 font=('华文行楷',50),
                 fg='red',
                 image=self.backim,
                 compound='center').pack(anchor='center',expand=1)

        # 绑定事件
        self.top.bind(sequence='<Key>', func=self.KeyBoard)

    def KeyBoard(self,event):
        self.top.destroy()
        gui = hp.GUIHomePage()
        gui.RunGUIHomePage()

    # 运行程序
    def RunGUIEndLuckyDraw(self):
        self.top.mainloop()

if __name__ == '__main__':
    gui = GUIEndLuckyDraw()
    gui.RunGUIEndLuckyDraw()

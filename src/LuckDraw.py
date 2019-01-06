# -*- coding:utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import random
import Image
import Tkinter as tk
from PIL import Image, ImageTk
import HomePage as hp
import AdjustPhoto as adjph
import EndLuckyDraw as eld


# ---------开始抽奖--------- #
class GUILuckDraw:

    # 初始化界面
    def __init__(self):
        # 初始化界面
        self.top = tk.Tk()
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        self.top.geometry("%dx%d" % (w, h))
        self.top.title('方圆羽毛球俱乐部2019年庆')
        backpath = os.path.abspath('..')+'/Image/system/luckydraw.png'
        self.backim = tk.PhotoImage(file=backpath)
        tk.Label(self.top,image=self.backim,compound='center').pack()

        # 回到主界面按钮
        iconpath = os.path.abspath('..')+'/Image/system/主页图标.png'
        self.icon = tk.PhotoImage(file=iconpath)
        tk.Button(self.top,
                  image=self.icon,
                  command=self.BackHomePage).place(x=1810, y=0)

        # 绑定事件
        self.top.bind(sequence='<Key>',func=self.StartStop)
        self.counter = 0

    # 抽奖
    def StartStop(self,event):
        # -------两人一组互换礼物(一次出现一个)------- #
        infile = os.path.abspath('..')+'/Image/Adjust'
        adj = adjph.AdjustPhoto()
        dir = adj.ObtainAddress(file_dir=infile)
        if len(dir) == 0 or len(dir) == 1:
            self.top.destroy()
            gui = eld.GUIEndLuckyDraw()
            gui.RunGUIEndLuckyDraw()
        else:
            if event.char == ' ':
                if self.counter<4:
                    self.counter = self.counter+1
                else:
                    self.counter = 1
            else:
                pass
            # print(self.counter)
            if self.counter==1:
                # 创建随机数
                self.rannum_1 = random.randint(0, len(dir) - 1)
                while 1:
                    self.rannum_2 = random.randint(0,len(dir)-1)
                    if self.rannum_1 != self.rannum_2:
                        break
                        pass
                    pass
                # 左边照片
                self.p1 = Image.open(dir[self.rannum_1])
                (x,y) = self.p1.size
                if x==600:
                    placex = 200
                    placey = 50+(800-y)/2
                else:
                    placey = 50
                    placex = (600-x)/2+200
                self.tkImage1 = ImageTk.PhotoImage(image=self.p1)
                self.Left_Image = tk.Label(self.top, image=self.tkImage1)
                self.Left_Image.place(x=placex, y=placey)
            elif self.counter == 2:
                # 右边照片
                self.p2 = Image.open(dir[self.rannum_2])
                (x, y) = self.p2.size
                if x == 600:
                    placex = 1050
                    placey = 50 + (800 - y) / 2
                else:
                    placey = 50
                    placex = (600 - x) / 2 + 1050
                self.tkImage2 = ImageTk.PhotoImage(image=self.p2)
                self.Right_Image = tk.Label(self.top, image=self.tkImage2)
                self.Right_Image.place(x=placex, y=placey)
            elif self.counter == 3:
                dir_left = dir[self.rannum_1]
                dir_right = dir[self.rannum_2]
                a = dir_left.split('/')
                a = a[-1]
                b = dir_right.split('/')
                b = b[-1]
                txt_left = a.split('.')
                txt_right = b.split('.')
                txt_left = txt_left[1]
                txt_right = txt_right[1]
                self.txt1 = tk.Label(self.top,text=txt_left,font=('华文行楷',70),bg='white')
                self.txt1.place(x=400,y=890)
                self.txt2 = tk.Label(self.top,text=txt_right,font=('华文行楷', 70),bg='white')
                self.txt2.place(x=1250, y=890)
            elif self.counter == 4:
                self.Left_Image.destroy()
                self.Right_Image.destroy()
                self.txt1.destroy()
                self.txt2.destroy()
                r = dir[self.rannum_2]
                os.remove(dir[self.rannum_1])
                dir = adj.ObtainAddress(file_dir=infile)
                for i in range(len(dir)):
                    if r == dir[i]:
                        os.remove(dir[i])
                        break

        # # -------两人一组互换礼物(同时出现)------- #
        # infile = os.path.abspath('..') + '/Image/Adjust'
        # adj = adjph.AdjustPhoto()
        # dir = adj.ObtainAddress(file_dir=infile)
        # if len(dir) == 0 or len(dir) == 1:
        #     self.top.destroy()
        #     gui = eld.GUIEndLuckyDraw()
        #     gui.RunGUIEndLuckyDraw()
        # else:
        #     if event.char == ' ':
        #         if self.counter < 3:
        #             self.counter = self.counter + 1
        #         else:
        #             self.counter = 1
        #     else:
        #         pass
        #     # print(self.counter)
        #     if self.counter == 1:
        #         # 创建随机数
        #         self.rannum_1 = random.randint(0, len(dir) - 1)
        #         while 1:
        #             self.rannum_2 = random.randint(0, len(dir) - 1)
        #             if self.rannum_1 != self.rannum_2:
        #                 break
        #                 pass
        #             pass
        #         # 左边照片
        #         self.p1 = Image.open(dir[self.rannum_1])
        #         (x, y) = self.p1.size
        #         if x == 600:
        #             placex = 200
        #             placey = 50 + (800 - y) / 2
        #         else:
        #             placey = 50
        #             placex = (600 - x) / 2 + 200
        #         self.tkImage1 = ImageTk.PhotoImage(image=self.p1)
        #         self.Left_Image = tk.Label(self.top, image=self.tkImage1)
        #         self.Left_Image.place(x=placex, y=placey)
        #         # 右边照片
        #         self.p2 = Image.open(dir[self.rannum_2])
        #         (x, y) = self.p2.size
        #         if x == 600:
        #             placex = 1050
        #             placey = 50 + (800 - y) / 2
        #         else:
        #             placey = 50
        #             placex = (600 - x) / 2 + 1050
        #         self.tkImage2 = ImageTk.PhotoImage(image=self.p2)
        #         self.Right_Image = tk.Label(self.top, image=self.tkImage2)
        #         self.Right_Image.place(x=placex, y=placey)
        #     elif self.counter == 2:
        #         dir_left = dir[self.rannum_1]
        #         dir_right = dir[self.rannum_2]
        #         a = dir_left.split('/')
        #         a = a[-1]
        #         b = dir_right.split('/')
        #         b = b[-1]
        #         txt_left = a.split('.')
        #         txt_right = b.split('.')
        #         txt_left = txt_left[1]
        #         txt_right = txt_right[1]
        #         self.txt1 = tk.Label(self.top, text=txt_left, font=('华文行楷', 70), bg='white')
        #         self.txt1.place(x=400, y=890)
        #         self.txt2 = tk.Label(self.top, text=txt_right, font=('华文行楷', 70), bg='white')
        #         self.txt2.place(x=1250, y=890)
        #     elif self.counter == 3:
        #         self.Left_Image.destroy()
        #         self.Right_Image.destroy()
        #         self.txt1.destroy()
        #         self.txt2.destroy()
        #         r = dir[self.rannum_2]
        #         os.remove(dir[self.rannum_1])
        #         dir = adj.ObtainAddress(file_dir=infile)
        #         for i in range(len(dir)):
        #             if r == dir[i]:
        #                 os.remove(dir[i])
        #                 break


        # -------轮次------- #
        # # 获取照片地址
        # infile = '/home/weiming/FangYuan/Image/Adjust'
        # adj = adjph.AdjustPhoto()
        # dir = adj.ObtainAddress(file_dir=infile)
        # # 决定谁第一个来抽奖
        # if event.char == 'a':
        #     print('press a')
        #     self.rannum_1 = random.randint(0,len(dir)-1)
        #     self.p1 = Image.open(dir[self.rannum_1])
        #     (x,y) = self.p1.size
        #     if x==600:
        #         placex = 200
        #         placey = 50+(800-y)/2
        #     else:
        #         placey = 50
        #         placex = (600-x)/2+200
        #     self.tkImage1 = ImageTk.PhotoImage(image=self.p1)
        #     self.Left_Image = tk.Label(self.top,image=self.tkImage1)
        #     self.Left_Image.place(x=placex,y=placey)
        #
        # # 开始抽奖
        # elif event.char == ' ':
        #     if len(dir) == 0 or len(dir) == 1:
        #         tkm.showinfo(title='提示', message='抽奖结束')
        #     else:
        #         while 1:
        #             self.rannum_2 = random.randint(0,len(dir)-1)
        #             if self.rannum_1 != self.rannum_2:
        #                 break
        #         self.p2 = Image.open(dir[self.rannum_2])
        #         (x, y) = self.p2.size
        #         if x == 600:
        #             placex = 1050
        #             placey = 50 + (800 - y) / 2
        #         else:
        #             placey = 50
        #             placex = (600 - x) / 2 + 1050
        #         self.tkImage2 = ImageTk.PhotoImage(image=self.p2)
        #         self.Right_Image = tk.Label(self.top, image=self.tkImage2)
        #         self.Right_Image.place(x=placex, y=placey)
        #
        # # 抽奖结束照片移到左边
        # elif event.char == '\r':
        #     (x, y) = self.p2.size
        #     if x==600:
        #         placex = 200
        #         placey = 50+(800-y)/2
        #     else:
        #         placey = 50
        #         placex = (600-x)/2+200
        #     self.Left_Image.destroy()
        #     self.Right_Image.destroy()
        #     self.tkImage1 = ImageTk.PhotoImage(image=self.p2)
        #     self.Left_Image = tk.Label(self.top, image=self.tkImage1)
        #     self.Left_Image.place(x=placex, y=placey)
        #     now = dir[self.rannum_2]
        #     os.remove(dir[self.rannum_1])
        #     dir = adj.ObtainAddress(file_dir=infile)
        #     for i in range(len(dir)):
        #         if now == dir[i]:
        #             self.rannum_1 = i


    # 返回主页
    def BackHomePage(self):
        self.top.destroy()
        gui = hp.GUIHomePage()
        gui.RunGUIHomePage()

    # 运行程序
    def RunGUILuckDraw(self):
        self.top.mainloop()

if __name__ == '__main__':
    gui = GUILuckDraw()
    gui.RunGUILuckDraw()
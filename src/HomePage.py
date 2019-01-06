# -*- coding:utf-8 -*-

import os
import subprocess
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import Tkinter as tk
import tkMessageBox as tkm
import RecordMessage as record
import LuckDraw as lucktdraw
import AdjustPhoto as adjph
import Music
import Video
import Cycle


# ---------系统主界面--------- #
class GUIHomePage:

    # 初始化
    def __init__(self):
        # 初始化界面
        self.top = tk.Tk()
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        self.top.geometry("%dx%d" % (w, h))
        self.top.title('方圆羽毛球俱乐部2019年庆')
        # 设置背景
        backpath = os.path.abspath('..') + '/Image/system/background.png'
        self.photo = tk.PhotoImage(file=backpath)
        self.background = tk.Label(self.top,
                                   text='方圆羽毛球俱乐部2019年年庆',
                                   font=('华文新魏', 95,"bold"),
                                   fg='black',
                                   image=self.photo,
                                   compound='center')
        self.background.pack()

        # ---菜单栏--- #
        menubar = tk.Menu(self.top)  # 初始化菜单栏
        # 创建“文件”下拉菜单
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="参会人员信息录入", command=self.File_RecordMessage)
        filemenu.add_command(label="修改参会人员信息", command=self.File_RenewMessage)
        filemenu.add_separator()  # 分割线
        filemenu.add_command(label="退出", command=self.File_Quit)
        # 创建“活动”下拉菜单
        activitymenu = tk.Menu(menubar, tearoff=0)
        activitymenu.add_command(label="开始抽奖", command=self.Act_LuckyDraw)
        activitymenu.add_command(label="播放音乐", command=self.Act_music)
        activitymenu.add_command(label="播放视频", command=self.Act_video)
        # 创建“帮助”下拉菜单
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="用户指南", command=self.Help_UsersGuide)
        helpmenu.add_command(label="快捷键", command=self.Help_HotKey)
        helpmenu.add_command(label="关于", command=self.Help_About)
        # 添加进入菜单栏
        menubar.add_cascade(label='文件', menu=filemenu)
        menubar.add_cascade(label='活动', menu=activitymenu)
        menubar.add_cascade(label='帮助', menu=helpmenu)
        # 将菜单栏加入窗口
        self.top.config(menu=menubar)

        # 绑定事件
        self.top.bind(sequence='<Key>', func=self.StartStop)

    # 参会人员信息录入
    def File_RecordMessage(self):
        tkm.showinfo(title='未完', message='未完')
        # self.top.destroy()
        # gui = record.GUIRecordMessage()
        # gui.RunGUIRecordMessage()

    # 修改参会人员信息
    def File_RenewMessage(self):
        tkm.showinfo(title='未完', message='未完')

    # 是否确定退出
    def File_Quit(self):
        if tkm.askyesno(title='确定退出', message='确定退出？'):
            self.top.destroy()

    # 相应快捷键
    def StartStop(self,event):
        if event.char=='\r':
            self.Act_LuckyDraw()
        elif event.char=='m':
            self.Act_music()
        elif event.char=='v':
            self.Act_video()
        elif event.char=='c':
            self.Act_Cycle()
        elif event.char=='p':
            ppt_dir = os.path.abspath('..')+'/ppt/方圆年庆颁奖.pptx'
            subprocess.call(['xdg-open', ppt_dir])


    # 开始抽奖
    def Act_LuckyDraw(self):
        # adj = adjph.AdjustPhoto()
        # infile = os.path.abspath('..')+'/Image/photo'
        # outfile = os.path.abspath('..')+'/Image/Adjust/'
        # dir = adj.ObtainAddress(file_dir=infile)
        # for i in range(len(dir)):
        #     photo = adj.ReadPhoto(address=dir[i])
        #     (x_s, y_s) = adj.ReSize(photo=photo)
        #     a = dir[i]
        #     b = a.split('/')
        #     outdir = outfile + b[-1]
        #     adj.OutPutPhoto(photo=photo, address=outdir, x_s=x_s, y_s=y_s)
        self.top.destroy()
        gui = lucktdraw.GUILuckDraw()
        gui.RunGUILuckDraw()

    # 循环照片
    def Act_Cycle(self):
        gui = Cycle.GUICycle()
        gui.RunGUICycle()

    # 播放音乐
    def Act_music(self):
        gui = Music.GUIMusic()
        gui.RunGUIMusic()

    # 播放视频
    def Act_video(self):
        gui = Video.GUIVideo()
        gui.RunGUIVdieo()

    # 用户指南
    def Help_UsersGuide(self):
        path = os.path.abspath('..')+'/Guide/用户指南'
        f = open(path, 'r')
        s = f.read()
        f.close()
        tkm.showinfo(title='用户指南', message=s)

    # 快捷键大全
    def Help_HotKey(self):
        path = os.path.abspath('..') + '/Guide/快捷键大全'
        f = open(path, 'r')
        s = f.read()
        f.close()
        tkm.showinfo(title='快捷键', message=s)

    # 关于
    def Help_About(self):
        tkm.showinfo(title='关于', message='作者：陈玮铭\n版本：V1.0\n联系方式：chen_wm97@qq.com\n感谢您的使用！')

    # 运行程序
    def RunGUIHomePage(self):
        self.top.mainloop()



if __name__ == '__main__':
    gui = GUIHomePage()
    gui.RunGUIHomePage()
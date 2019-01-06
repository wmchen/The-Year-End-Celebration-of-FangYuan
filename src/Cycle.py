# -*- coding:utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import Tkinter as tk
import Image
from PIL import Image, ImageTk


# ---------循环--------- #
class GUICycle:

    # 初始化
    def __init__(self):
        # 初始化界面
        self.top = tk.Tk()
        w = self.top.winfo_screenwidth()
        h = self.top.winfo_screenheight()
        self.top.geometry("%dx%d" % (w, h))
        self.top.title('方圆羽毛球俱乐部年度庆典抽奖系统')
        self.canvas = tk.Canvas(self.top, width=w, height=h, bg='white')

        self.counter = 1
        while self.counter<=25:
            filename = os.path.abspath('..') + '/Image/cycle/' + str(self.counter) + '.png'
            if os.path.isfile(filename):
                self.im = Image.open(filename)
                # im1 = Image.fromarray(cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB))
                self.tkImage = ImageTk.PhotoImage(image=self.im)
                # img = ImageTk.PhotoImage(file = filename)
                itext = self.canvas.create_image((960, 540), image=self.tkImage)
                self.canvas.pack()
                self.top.update()
                self.top.after(10000)
                self.counter+=1
                if self.counter>25:
                    self.counter=1




    # def cycleimage(self):
    #     adj = adjph.AdjustPhoto()
    #     dir = adj.ObtainAddress(file_dir=filedir)
    #     self.p1 = Image.open(dir[self.counter])
    #     self.tkImage1 = ImageTk.PhotoImage(image=self.p1)
    #     tk.Label(self.top,image=self.tkImage1).pack()



    def RunGUICycle(self):
        self.top.mainloop()


if __name__ == '__main__':
    gui = GUICycle()
    gui.RunGUICycle()
# -*- coding:utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import Tkinter as tk
import ttk
import subprocess

# ---------系统主界面--------- #
class GUIVideo:

    #初始化
    def __init__(self):
        #初始化界面
        self.top = tk.Tk()
        # curWidth = 450
        # curHeight = 300
        # sw = self.top.winfo_screenwidth()
        # sh = self.top.winfo_screenheight()
        # x = (sw - curWidth) / 2
        # y = (sh - curHeight) / 2
        # cursize = '%dx%d+%d+%d' % (curWidth, curHeight, x, y)
        # self.top.geometry(cursize)
        self.top.title('播放视频')

        #创建下拉列表
        self.comvalue = tk.StringVar()
        self.comlist = ttk.Combobox(self.top,textvariable=self.comvalue)
        self.comlist["values"] = ("倒计时","荷塘月色","驻外视频","难忘今宵")
        self.comlist.grid(row=0,column=0)

        #播放按钮
        tk.Button(self.top,
                  text='播放',
                  command=self.getname).grid(row=0,column=1)

    def getname(self):
        filename = self.comlist.get()
        if filename=='倒计时':
            file = os.path.abspath('..') + '/media/倒计时.mp4'
        elif filename=='荷塘月色':
            file = os.path.abspath('..') + '/media/荷塘月色背景.mp4'
        elif filename=='驻外视频':
            file = os.path.abspath('..') + '/media/驻外.mp4'
        elif filename=='难忘今宵':
            file = os.path.abspath('..') + '/media/难忘今宵.mp4'
        self.play(file)

    def play(self,file):
        # chunk = 1  # 指定WAV文件的大小
        # wf = wave.open(file, 'rb')  # 打开WAV文件
        # p = pyaudio.PyAudio()  # 初始化PyAudio模块
        #
        # # 打开一个数据流对象，解码而成的帧将直接通过它播放出来，我们就能听到声音啦
        # stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
        #                 rate=wf.getframerate(), output=True)
        #
        # data = wf.readframes(chunk)  # 读取第一帧数据
        # print(data)  # 以文本形式打印出第一帧数据，实际上是转义之后的十六进制字符串
        #
        # # 播放音频，并使用while循环继续读取并播放后面的帧数
        # # 结束的标志为wave模块读到了空的帧
        # while data != b'':
        #     stream.write(data)  # 将帧写入数据流对象中，以此播放之
        #     data = wf.readframes(chunk)  # 继续读取后面的帧
        #     # dump_buff_file.write(str(data) + "\n---------------------------------------\n")  # 将读出的帧写入文件中，每一个帧用分割线隔开以便阅读
        #
        # stream.stop_stream()  # 停止数据流
        # stream.close()  # 关闭数据流
        # p.terminate()  # 关闭 PyAudio
        # print('play函数结束！')
        subprocess.call(['xdg-open', file])
        self.top.destroy()

    def RunGUIVdieo(self):
        self.top.mainloop()

if __name__ == '__main__':
    gui = GUIVideo()
    gui.RunGUIVdieo()
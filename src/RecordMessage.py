# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import Tkinter as tk
import tkMessageBox as tkm
import DataBaseOperate as dbo
import config as cfg
import HomePage as hp



# ---------参会人员信息录入--------- #
class GUIRecordMessage:

    # 初始化
    def __init__(self):
        # 初始化界面
        self.top = tk.Tk()
        curWidth = 450
        curHeight = 300
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()
        x = (sw - curWidth) / 2
        y = (sh - curHeight) / 2
        cursize = '%dx%d+%d+%d' % (curWidth, curHeight, x, y)
        self.top.geometry(cursize)
        self.top.title('参会人员信息录入')

        # 添加信息
        tk.Label(self.top,text='姓名：',font=('',13)).place(x=85,y=30)
        tk.Label(self.top, text='性别：', font=('', 13)).place(x=85,y=90)
        tk.Label(self.top, text='是否交照片：', font=('', 13)).place(x=35,y=150)

        # 姓名
        self.nameVar = tk.StringVar()
        self.name = tk.Entry(self.top,
                             textvariable=self.nameVar,
                             width=20,
                             font=('',13))
        self.name.place(x=185,y=30)
        # 性别
        self.sexVar = tk.IntVar()
        tk.Radiobutton(self.top,text='男',variable=self.sexVar,font=('', 13),value=1).place(x=170,y=90)
        tk.Radiobutton(self.top,text='女',variable=self.sexVar,font=('', 13),value=0).place(x=250, y=90)
        # 是否已交照片
        self.if_imageVar = tk.IntVar()
        tk.Radiobutton(self.top,text='是',font=('', 13),variable=self.if_imageVar,value=1).place(x=170,y=150)
        tk.Radiobutton(self.top,text='否',font=('',13),variable=self.if_imageVar,value=0).place(x=250, y=150)
        # ---按钮--- #
        tk.Button(self.top,
                  text='保存',
                  font=('', 13),
                  command=self.SaveAsk).place(x=140, y=220)
        tk.Button(self.top,
                  text='退出',
                  font=('', 13),
                  command=self.Quit).place(x=260, y=220)

    # 是否确定退出
    def Quit(self):
        if tkm.askyesno(title='确定退出', message='您还未保存信息，确定退出？'):
            self.top.destroy()
            gui = hp.GUIHomePage()
            gui.RunGUIHomePage()

    # 是否确定保存
    def SaveAsk(self):
        self.SaveIntoDataBase()

    # 保存进入数据库
    def SaveIntoDataBase(self):
        DataBase = dbo.DataBaseOperate()
        # 获取数据
        db_name = '\"' + self.name.get() + '\"'
        db_sex = self.sexVar.get()
        db_sex = str(db_sex)
        db_im = self.if_imageVar.get()
        db_im = str(db_im)
        db_tn = cfg.Table_Name
        db_attr = cfg.AttributeName
        data_size = 1
        data = [[db_name,db_sex,db_im]]
        print(data)
        # 写入数据库
        DataBase.InsertData(table_name=db_tn,
                            attribute_name=db_attr,
                            data_size=data_size,
                            data=data,
                            is_test=False)
        # 恢复主键
        sql_key = "alter table Information drop FangYuan_id;"
        DataBase.cursor.execute(sql_key)
        sql_key = "ALTER TABLE Information ADD FangYuan_id INT NOT NULL FIRST;"
        DataBase.cursor.execute(sql_key)
        sql_key = "ALTER TABLE Information MODIFY COLUMN FangYuan_id INT NOT NULL AUTO_INCREMENT,ADD PRIMARY KEY (FangYuan_id);"
        DataBase.cursor.execute(sql_key)
        DataBase.connection.commit()
        # 保存成功
        DataBase.CloseDatabaseConnection()
        self.SaveSuccessful()

    # 保存成功
    def SaveSuccessful(self):
        # 保存完毕回到主页
        tkm.showinfo(title='保存成功', message='恭喜你，保存成功！')
        self.top.destroy()
        gui = hp.GUIHomePage()
        gui.RunGUIHomePage()

    # 运行程序
    def RunGUIRecordMessage(self):
        self.top.mainloop()


if __name__ == '__main__':
    gui = GUIRecordMessage()
    gui.RunGUIRecordMessage()
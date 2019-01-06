# -*- coding:utf-8 -*-


import pymysql
import config as cfg


class DataBaseOperate(object):

    def __init__(self):
        self.host = cfg.HostIP
        self.user = cfg.UserName
        self.password = cfg.DataBasePassword
        self.database = cfg.DataBaseName
        self.port = cfg.PortNum
        self.charset = cfg.CodingChartSet
        # 创建连接
        self.connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     database=self.database,
                                     port=self.port,
                                     charset=self.charset)
        # 创建游标
        self.cursor = self.connection.cursor()
        pass




    # ********创建数据表格******** #
    # table_name: 表格名称
    # attribute_num: 字段数目
    # attribute_name: 字段名称，list
    # attribute_config: 字段属性，list
    # data_size: 数据量
    # index_name: 增加或指定的索引的名称
    # is_index: 是否需要索引，True--需要，False--不需要
    # data: 数据
    # is_test: 是否为测试，True--结果不上传至数据库；False--结果上传至数据库
    def CreateTable(self,
                    table_name,
                    attribute_num,
                    attribute_name,
                    attribute_config,
                    data_size,
                    data,
                    index_name='ID',
                    is_test=True):
        connection = self.connection
        cursor = self.cursor
        list_attri_NameANDConfig = []
        for i in range(attribute_num):
            list_nameplusconfig = attribute_name[i] + ' ' + attribute_config[i]
            str_nameplusconfig = ''.join(list_nameplusconfig)
            list_attri_NameANDConfig.append(str_nameplusconfig)
        str_attri_NameANDConfig = ','.join(list_attri_NameANDConfig)
        str_attri_Name = ','.join(attribute_name)
        # 创建表格
        if index_name=='ID':
            sql_create = "CREATE TABLE IF NOT EXISTS {table}(ID INT NOT NULL AUTO_INCREMENT,{content},PRIMARY KEY (ID))".format(table=table_name,
                                                                                                                                content=str_attri_NameANDConfig)
            cursor.execute(sql_create)
        else:
            sql_create = "CREATE TABLE IF NOT EXISTS {table}({content},PRIMARY KEY ({index_name}))".format(table=table_name,
                                                                                                           content=str_attri_NameANDConfig,
                                                                                                           index_name=index_name)
        cursor.execute(sql_create)


        # 创建索引
        if index_name == 'ID':
            sql_index = "ALTER TABLE {table} ADD UNIQUE (ID)".format(table=table_name)
            cursor.execute(sql_index)
        else:
            sql_index = "ALTER TABLE {table} ADD UNIQUE ({index_name})".format(table=table_name,index_name=index_name)
            cursor.execute(sql_index)
        # 插入内容
        for i in range(data_size):
            list_data = data[i][:]
            str_data = ','.join(list_data)
            if index_name=='ID':
                sql_data = "INSERT INTO {table}(ID,{attribute_name}) VALUES(NULL,{data})".format(table=table_name,
                                                                                                 attribute_name=str_attri_Name,
                                                                                                 data=str_data)
            else:
                sql_data = "INSERT INTO {table}({attribute_name}) VALUES({data})".format(table=table_name,
                                                                                         attribute_name=str_attri_Name,
                                                                                         data=str_data)
            cursor.execute(sql_data)

        # 改变数据表内容
        if is_test==False:
            connection.commit()




    # ********向数据表中插入数据******** #
    # table_name: 表格名称
    # attribute_name: 字段名称，list
    # data_size: 数据量
    # data: 数据
    # is_test: 是否为测试，True--结果不上传至数据库；False--结果上传至数据库
    def InsertData(self,
                   table_name,
                   attribute_name,
                   data_size,
                   data,
                   is_test=True):
        connection = self.connection
        cursor = self.cursor
        str_attri_Name = ','.join(attribute_name)
        for i in range(data_size):
            list_data = data[i][:]
            str_data = ','.join(list_data)
            sql_insert = "INSERT INTO {table}({attribute_name}) VALUES({data})".format(table=table_name,
                                                                                        attribute_name=str_attri_Name,
                                                                                        data=str_data)
            cursor.execute(sql_insert)
        # 改变数据表内容
        if is_test == False:
            connection.commit()





    # ********查询数据表中数据******** #
    def SearchData(self,table_name):
        cursor = self.cursor
        # 查询
        sql_select = "SELECT * from {table_name};".format(table_name=table_name)
        cursor.execute(sql_select)
        cursor.rowcount
        get_row = cursor.fetchall()
        row_num = get_row.__len__()
        data = []
        for i in range(row_num):
            data_row = get_row[i][:]
            data_row = list(data_row)
            for j in range(1,len(cfg.RenterMessage_AttributeName)):
                # item = data_row[j]
                # item = item.encode('utf8')
                # data_row[j] = item
                data_row[j] = data_row[j].encode('utf8')
            data.append(data_row)
        # 打印
        return data

    # ********查询登录密码******** #
    def SeeLoginPassword(self,table_name):
        cursor = self.cursor
        # 查询
        sql_select = "SELECT * from {table_name};".format(table_name=table_name)
        cursor.execute(sql_select)
        cursor.rowcount
        get_row = cursor.fetchall()
        row_num = get_row.__len__()
        data = get_row[0][1]
        data = data.encode('utf8')
        return data


    # ********删除操作，可删除数据库、数据表、数据表中的数据******** #
    # database_name: 数据库的名称(is_database=True时填写)
    # table_name: 表格的名称
    # deletenum: 删除表格中数据的数目(is_specific=False时填写)
    # specificnum: 删除表格中特定行的数据(is_specific=True时填写)
    # order='back'从列表后面删除   order='front'从列表前面删除
    # is_database: 是否删除数据库，默认为否
    # is_table: 是否删除表格，默认为否
    # is_all: 是否删除表格中所有数据，默认为否
    # is_specific: 是否删除表格中特定行的数据，默认为是
    # is_test: 是否为测试，True--结果不上传至数据库；False--结果上传至数据库
    def DeleteData(self,
                   database_name=None,
                   table_name=None,
                   deletenum=None,
                   specificnum=None,
                   order='back',
                   is_database=False,
                   is_table=False,
                   is_all=False,
                   is_specific=True,
                   is_test=True):
        connection = self.connection
        cursor = self.cursor
        if is_database:
            sql = "drop database {database}".format(database=database_name)
        else:
            if is_table:
                sql = "drop table {table}".format(table=table_name)
            else:
                if is_all:
                    sql = "delete from {table}".format(table=table_name)
                else:
                    if is_specific:
                        sql = "delete from {table} where id={index}".format(table=table_name,index=specificnum-1)
                    else:
                        if order=='back':
                            for i in deletenum:
                                get_row = cursor.fetchall()
                                row_num = get_row.__len__()
                                sql = "delete from {table} where id={index}".format(table=table_name,index=row_num-1)
                        elif order=='front':
                            for i in deletenum:
                                sql = "delete from {table} where id=0".format(table=table_name)
                        else:
                            print("Order Input Error!")
        cursor.execute(sql)
        if is_test==False:
            connection.commit()




    # ********关闭数据库连接******** #
    def CloseDatabaseConnection(self):
        connection = self.connection
        connection.close()
        pass


    pass

if __name__ == '__main__':

    db = DataBaseOperate()

    # 创建数据表
    # # 当前
    # tablelist = []
    # for i in range(len(cfg.PropertyTable)):
    #     tablelist.append(cfg.PropertyTable[i][1])
    #
    # # 过往
    # Past_tablelist = []
    # for i in range(len(cfg.Past_PropertyTable)):
    #     Past_tablelist.append(cfg.Past_PropertyTable[i][1])
    #
    #
    #
    # attribute_name = cfg.RenterMessage_AttributeName
    # attribute_num = len(attribute_name)
    # attribute_config = []
    # for i in range(attribute_num):
    #     if attribute_name[i]=='备注':
    #         attribute_config.append("VARCHAR(100)")
    #     else:
    #         attribute_config.append("VARCHAR(50)")
    # data_size = 0
    # data = [""]
    # for i in range(len(Past_tablelist)):
    #     db.CreateTable(table_name=Past_tablelist[i],
    #                    attribute_num=attribute_num,
    #                    attribute_name=attribute_name,
    #                    attribute_config=attribute_config,
    #                    data_size=data_size,
    #                    data=data,
    #                    is_test=False)

    # insert into LoginPassword (登录密码) values ("676597");
    # select * from LoginPassword;

    # table_name = cfg.PasswordTable
    # attribute_name = [cfg.PasswordTable_Attr]
    # data = [["\""+"affeng82"+"\""]]
    # db.InsertData(table_name=table_name,
    #               attribute_name=attribute_name,
    #               data_size=1,
    #               data=data,
    #               is_test=False)


    # 插入数据
    # data_size = 1
    # data = [["\"陈玮铭\"","0","1"]]
    # db.InsertData(table_name="Information",
    #               attribute_name=["FangYuan_name","FangYuan_sex","FangYuan_image"],
    #               data_size=data_size,
    #               data=data,
    #               is_test=False)

    # table_name = cfg.PasswordTable
    # attribute_name = cfg.PasswordTable_Attr



    # 查询密码
    # data = db.SeeLoginPassword(table_name="LoginPassword")
    # print(data)

    # 查询数据
    # data = db.SearchData(table_name="ShuiDianSuo_603")
    # print(len(data))


    # 清空数据表
    # for i in range(len(tablelist)):
    #     db.DeleteData(table_name=tablelist[i],
    #                   is_all=True,
    #                   is_test=False)
    #



    db.DeleteData(table_name="Information",
                              is_all=True,
                              is_test=False)


    # # 删除数据表
    # for i in range(len(tablelist)):
    #     db.DeleteData(table_name=tablelist[i],
    #                   is_table=True,
    #                   is_test=False)


    # # 删除数据库
    # db.DeleteData(database_name=cfg.DataBaseName,
    #               is_database=True)



    db.CloseDatabaseConnection()



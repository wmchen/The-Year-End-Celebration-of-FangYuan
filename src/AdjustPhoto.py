# -*- coding:utf-8 -*-

import os
import Image as im


class AdjustPhoto:

    def __init__(self):
        pass

    # 获取图片地址
    def ObtainAddress(self,file_dir):
        Dir = []
        for root,dirs,files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.png':
                    Dir.append(os.path.join(root,file))
        return Dir

    # 读取图片
    def ReadPhoto(self,address):
        photo = im.open(address)
        return photo

    # 调整图片尺寸
    def ReSize(self,photo):
        (x,y) = photo.size
        if x<=y:
            y_s = 800
            x_s = x*y_s/y
        else:
            x_s = 600
            y_s = y*x_s/x
            pass
        return x_s,y_s

    # 输出图片
    def OutPutPhoto(self,photo,address,x_s,y_s):
        out = photo.resize((x_s,y_s),im.ANTIALIAS)
        out.save(address)

if __name__ == '__main__':
    adj = AdjustPhoto()
    infile = os.path.abspath('..') + '/Image/photo/'
    outfile = os.path.abspath('..') + '/Image/Adjust/'
    dir = adj.ObtainAddress(file_dir=infile)
    for i in range(len(dir)):
        photo = adj.ReadPhoto(address=dir[i])
        (x_s,y_s) = adj.ReSize(photo=photo)
        a = dir[i]
        b = a.split('/')
        outdir = outfile + b[-1]
        adj.OutPutPhoto(photo=photo,address=outdir,x_s=x_s,y_s=y_s)
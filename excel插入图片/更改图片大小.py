#encoding:utf-8
"""
@project=企查查
@file=tupiancharubiaoge
@author=hjfan
@create_time:2021/8/19 17:52
"""
import shutil

import xlrd
import xlwt
import xlsxwriter
import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS)
  #resize image with high-quality
  out.save(fileout)


def gengai():
    shutil.rmtree(r'D:\\企查查\\photo_update')

    os.mkdir(r'D:\\企查查\\photo_update')
    for root, dirs, files in os.walk('D:\企查查\yiyue_pic_aa_test_ten'):
        for file in files:
            # print(file)
            width = 150
            height = 150
            aa = 'D:\\企查查\\photo_update'+"\\"+file
            # print(root+"\\"+file)
            try:
                ResizeImage(root+"\\"+file, aa, width, height)
            except:
                print(file)

    return "图片大小更改完成"





#encoding:utf-8
"""
@project=企查查
@file=匹配相同测试
@author=hjfan
@create_time:2021/8/28 15:37
"""


import os
import warnings
import pandas as pd
warnings.filterwarnings("ignore")



import xlrd
import xlsxwriter
from xlsxwriter import workbook
from openpyxl import load_workbook
from openpyxl.drawing.image import Image


def charu_pictrue(write_excel_path,read_excel_path,sheet_index,sheet_name,picture_url,picture_path):

    wb = load_workbook(read_excel_path)
    sheet = wb.active

    cell = sheet[sheet_index]

    ws=wb[sheet_name]

    cell.value = picture_url


    data = pd.read_excel(read_excel_path)
    data_list = [data.loc[i].to_dict() for i in data.index.values]

    for file in os.listdir(picture_path):
        for i in data_list:
            file = str(file.replace(".jpg",''))

            # i["taobao_goods_id"] = str(i["taobao_goods_id"]).replace(".0","")
            if str(i["taobao_goods_id"]) == file:
                suoyin = data_list.index(i)+2
                # print(i["taobao_goods_id"])
                img = Image(picture_path+"\\"+str(i["taobao_goods_id"])+".jpg")
                print(img)
                ws.add_image(img,'H{}'.format(suoyin))

    wb.save(write_excel_path)
    return "插入完成，程序结束！！！"

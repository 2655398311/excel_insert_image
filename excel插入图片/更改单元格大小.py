#encoding:utf-8
"""
@project=企查查
@file=更改单元格大小
@author=hjfan
@create_time:2021/8/27 15:40
"""


import os
import xlwings as xw




def genggai_danyuange(path):
    app = xw.App(visible=True, add_book=False)

    file_path = "存放excel文件"

    file_list = os.listdir(file_path)
    for i in file_list:
        file_paths = os.path.join(file_path,i)
        workbook = app.books.open(file_paths)

        for j in workbook.sheets:
            for a in range(1,10):
                for aa in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:

                    value = j.range("{}{}".format(aa,a)).expand("table")

                    # value1 = j.range("A2").expand("table")
                    value.column_width = 25
                    value.row_height = 120

        workbook.save(path)
        return "更改单元格大小完成"


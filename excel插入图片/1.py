#encoding:utf-8
"""
@project=python图片自动化
@file=1
@author=2242
@create_time=2021/9/17 13:58

"""

import re
import warnings
import pandas as pd
pd.set_option('display.width', 180)  # 150，设置打印宽度
pd.set_option('display.max_columns', 100) # 打印最大列数
import requests
import multiprocessing

warnings.filterwarnings("ignore")
data = pd.read_excel(r"C:\Users\2242\Desktop\plusmall竞店爆款.xlsx",sheet_name='2020年8月9月')
print(data.head())
import math
import json
import shutil
import warnings
import requests
import re,os,time
import datetime
import urllib
import pandas as pd
from PIL import Image
from io import BytesIO
import gevent
from gevent import monkey, pool
from sqlalchemy import create_engine


def req(result):
    b = str(result['taobao_goods_id'])
    c = str(result["month_id"])

    re_images = re.sub('https:|http:', '', result['taobao_goods_pictrue_url'])
    r = requests.get('http:' + re_images)
    aa_code = r.status_code
    print(aa_code)
    path = r"D:\\企查查\\yiyue_pic_aa_test_ten\\" + b + '.jpg'
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
def main(pool,path,sheet_name,count = 0):
    shutil.rmtree(r'D:\\企查查\\yiyue_pic_aa_test_ten')
    os.mkdir(r'D:\\企查查\\yiyue_pic_aa_test_ten')

    # data = pd.read_excel(r"D:\企查查\易月插入图片\plusmall竞店爆款.xlsx", sheet_name='2020年8月9月')
    data = pd.read_excel(path, sheet_name=sheet_name)
    data = data.dropna()
    data_list = [data.loc[i].to_dict() for i in data.index.values]
    process_list = []

    for i in data_list:
        process_list.append(pool.spawn(req, i))

        # print(len(process_list))
    gevent.joinall(process_list)
    count += 1

    return count

# if __name__ == '__main__':
#     aa = main(pool.Pool(200),path=r"D:\企查查\易月插入图片\plusmall竞店爆款.xlsx",sheet_name='2020年8月9月')
#     print(aa)
from 易月插入图片.图片下载协程 import *
from 易月插入图片.更改图片大小 import *
from 易月插入图片.更改单元格大小 import *
from 易月插入图片.匹配相同测试 import *




pic_download_count = main(pool.Pool(300), path=r"D:\企查查\易月插入图片\plusmall竞店爆款.xlsx", sheet_name='2020年8月9月')
if pic_download_count ==1:
    pic_big_small = gengai()
    if pic_big_small == "图片大小更改完成":
        danyuange_ = genggai_danyuange(path='sky_cat_update_v1.xlsx')
        if danyuange_ == "更改单元格大小完成":

            ##参数说明：
            '''
            write_excel_path:插入图片最终的结果表格，路径需要加上表格后缀。xlsx,csv.xls
            read_excel_path:更改单元格大小重新生成的表格结果路径，路径需要加上表格后缀。xlsx,csv.xls
            sheet_index：需要对表格中哪一列插入数据，例如 H1，I1，G1
            sheet_name：这个为表格中的工作sheet
            picture_url：这个位插入图片列的表头
            picture_path：这个为 更改图片大小后图片所在的文件夹
            
            '''
            result = charu_pictrue(write_excel_path='result.xlsx',read_excel_path='sky_cat_update_v1.xlsx',sheet_index='H1',sheet_name='2020年8月9月',picture_url='picture_url',picture_path=r'D:\企查查\photo_update')

            print(result)





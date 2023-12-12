import os
from operator import length_hint
import xlwings as wx

def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        # 排除临时的文件
        if '~$' in file:
            continue
        # 取得文件清单
        if ".mp4" in file:
            file_path = os.path.join(path, file)
            list_name.append(file_path)

def change_name(file_path, new_name, list_name):
    if(length_hint(new_name) != length_hint(list_name)):
        print("数目不对")
        return;
    # 逐个处理照片
    for i, filename in enumerate(list_name):
        old_name = (os.path.basename(filename)).split('.')[0]
        print(f'第{i}个文件名是{old_name}')
        nfname = file_path + os.sep + new_name[i] + ".mp4"
        print("新文件名" + nfname)
        os.rename(filename, nfname)

def main():
    file_path = input('输入文件夹路径:')  # 文件夹位置
    try:
        #读取文件夹下的所有文件
        List_files = []
        listdir(file_path, List_files)
        # 读取员工姓名和员工号，组成新的文件名
        new_name = ["01金融量化分析-基本金融知识介绍",
        "02金融量化分析-股票基本知识和股票分类",
        "03金融量化分析-股票市场构成",
        "04金融量化分析-影响股价因素、股票买卖知识",
        "05金融量化分析-金融分析",
        "06金融量化分析-金融量化投资介绍",
        "07金融量化分析-量化投资与Python、ipython初识",
        "08金融量化分析-ipython魔术命令",
        "09金融量化分析-ipython高级功能",
        "10金融量化分析-numpy-array基础",
        "11金融量化分析-numpy-array创建",
        "12金融量化分析-numpy-array索引和切片",
        "13金融量化分析-numpy-array布尔型索引",
        "14金融量化分析-numpy-array花式索引",
        "15金融量化分析-numpy-array通用函数",
        "16金融量化分析-numpy-统计方法和随机数生成",
        "17series介绍",
        "18series整数索引问题",
        "19series数据对齐",
        "20series缺失值处理",
        "21series小结",
        "22DataFrame的创建",
        "23DataFrame常用属性",
        "24DataFrame索引和切片",
        "25DataFrame数据对齐与缺失数据处理",
        "26pandas常用函数",
        "27时间处理对象",
        "28时间对象生成",
        "29时间序列",
        "30文件读取",
        "31文件操作3+pandas收尾",
        "32matplotlib介绍",
        "33plot函数周边",
        "34pandas与Matplotlib",
        "35使用matplotlib绘制数学函数图像",
        "36matplotlib 画布与子图",
        "37matplotlib 柱状图和饼图",
        "38matplotlib K线图",
        "39tushare包介绍",
        "40股票分析作业说明",
        "41股票分析作业",
        "42双均线分析作业说明",
        "43双均线分析作业1",
        "44双均线分析作业2",
        "45第一个量化策略-1",
        "46第一个量化策略-2",
        "47第一个量化策略-3",
        "48第一个量化策略-4",
        "49双均线策略-1",
        "50双均线策略-2",
        "51因子选股策略-1",
        "52因子选股策略-2",
        "53多因子选股策略",
        "54多因子选股策略实现",
        "55均值回归理论讲解",
        "56均值回归理论实现",
        "57布林带策略",
        "58布林带策略实现",
        "59PEG策略",
        "60PEG策略实现",
        "61动量策略vs反转策略",
        "62羊驼交易法则",
        "63简易回测框架介绍",
        "64上下文数据存储",
        "65获取历史数据",
        "66下单函数1",
        "67下单函数2",
        "68回测框架",
        "69回测框架展示",
        "70回测框架",
        "71回测框架展示"]
        # getinfo(new_name, index_file) #通过读取excel文件的名称，但是mac下wps调用不起来。
        # 修改文件名字
        change_name(file_path, new_name, List_files)

    except Exception as e:
        # 打印异常信息
        print(e)


if __name__ == '__main__':
    main()



# def getinfo(new_name, index_file):  # 获取人员姓名和编号
#     app = wx.App(spec='wpsoffice', visible=False, add_book=False)  # 不打开baiexcel
#     print("读取人员信息--->" + index_file)
#     wb = app.books.open(index_file)
#     sheet = wb.sheets[0]
#     nrows = sheet.used_range.last_cell.row  # 获取最大行数
#     ncolumns = sheet.used_range.last_cell.column  # 获取最大列数
#
#     # 查找姓名和编号的列
#     file_name = ""
#     empl_name = ""
#     empl_numb = ""
#     ename_col = 0
#     enumb_col = 0
#
#     print("最大列数--->" + str(ncolumns))
#
#     for col in range(1, ncolumns + 1):
#         if sheet.range((1, col)).value == "name":
#             ename_col = col
#             print("姓名的列--->" + str(col))
#
#         if sheet.range((1, col)).value == "number":
#             enumb_col = col
#             print("员工号的列--->" + str(col))
#
#     # 取行中的姓名和编号
#     for row in range(2, nrows + 1):
#         empl_name = str(sheet.range((row, ename_col)).value)
#         empl_numb = str(sheet.range((row, enumb_col)).value)
#         file_name = (empl_name + empl_numb).split('.')[0]  # 新的名字
#         print(file_name)
#         new_name.append(file_name)
#
#     print(new_name)
#
#     wb.close()
#     app.quit()
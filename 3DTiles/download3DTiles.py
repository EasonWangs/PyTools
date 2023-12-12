# coding=utf-8
from urllib import request
import os
import socket
import zlib

# python版本3.7
# 设置超时
socket.setdefaulttimeout(60)


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print('path create success!')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print('path already exist!')
        return False


# 定义要创建的目录
mkpath = "F:\\python\\cesiumData\\"


# 调用函数
# mkdir(mkpath)

def callbackfunc(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    # percent = 100.0 * blocknum * blocksize / totalsize
    # if percent > 100:
    # percent = 100
    print("--")


# 便利URL，获取数据
def getDataByUrl():
    str1 = "https://beta.cesium.com/api/assets/1461/"
    str2 = ".b3dm?access_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiMTBjN2E3Mi03ZGZkLTRhYmItOWEzNC1iOTdjODEzMzM5MzgiLCJpZCI6NDQsImlhdCI6MTQ4NjQ4NDM0M30.B3C7Noey3ZPXcf7_FXBEYwirct23fsUecRnS12FltN8&v=1.0"
    for z in range(0, 8):
        for x in range(0, 2 ** z):
            path = str(z) + "\\" + str(x)
            temppath = mkpath + path
            mkdir(temppath)
            for y in range(0, 2 ** z):
                url = str(z) + '/' + str(x) + '/' + str(y)
                str3 = str1 + url + str2
                try:
                    # urllib.urlretrieve(str3,url+'.b3dm')
                    req = request.Request(str3)
                    req.add_header('Host', 'beta.cesium.com')
                    req.add_header('Connection', 'keep-alive')
                    req.add_header('Origin', 'https://cesiumjs.org')
                    req.add_header('User-Agent',
                                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
                    req.add_header('Accept', '*/*')
                    req.add_header('Referer',
                                   'https://cesiumjs.org/NewYork/?view=-74.02572034279622%2C40.669539917125135%2C1364.6164107825127%2C21.27406391595569%2C-21.3627766554608%2C0.0706585523215407')
                    req.add_header('Accept-Encoding', 'gzip, deflate, br')
                    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
                    with request.urlopen(req) as f:
                        # print('Status:', f.status, f.reason)
                        # for k, v in f.getheaders():
                        # print('%s: %s' % (k, v))
                        f2 = open(url + '.b3dm', 'wb')
                        data = f.read()
                        html = zlib.decompress(data, 16 + zlib.MAX_WBITS)
                        f2.write(html)
                except Exception as e:
                    print(e)


getDataByUrl()
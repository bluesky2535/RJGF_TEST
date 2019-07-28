import  os
import time


if __name__ == '__main__':
    nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    os.mkdir('测试文件夹'+nowtime)
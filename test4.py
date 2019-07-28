import os
import time



if __name__ == '__main__':
    nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    os.mkdir('自行构建文件d夹'+nowtime)
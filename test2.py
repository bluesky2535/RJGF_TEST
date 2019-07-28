import os
import time

if __name__ == '__main__':
    nowtime=time.strftime('%Y%m%d%H%M%S',time.localtime())
    os.mkdir('自动构建'+nowtime)
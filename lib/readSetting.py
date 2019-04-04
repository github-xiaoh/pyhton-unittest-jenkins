# -*- coding:utf-8 -*-


import configparser
import os



def readconf():

    #用os模块来读取
    curpath=os.path.dirname(os.path.realpath(__file__))
    cfgpath=os.path.join(curpath,"/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/config/setting.ini")  #读取到本机的配置文件

    # print(cfgpath)
    conf = configparser.ConfigParser()
    conf.read(cfgpath,encoding='utf-8')

    logpath = conf.get('logFile','logpath')
    lognum = conf.get('logFile','logNum')

    config = {
        'logpath' : logpath,
        'lognum' : lognum,
    }

    return config



# print(readconf())



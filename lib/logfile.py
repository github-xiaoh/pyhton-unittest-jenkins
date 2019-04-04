# -*- coding:utf-8 -*-


import logging
import os
import time


# 定义log文件名字
# 创建一个logger
# 将log写在输入台
# 写在文件

def logger():

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)      # 定义logger日志等级

    log_path = '/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/log'
    logname = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))


    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(logname,'a',encoding='utf-8')
    fh.setLevel(logging.DEBUG)

    # 创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 定义handler输出到格式
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    # # 记录一条日志
    # if level == 'info':
    #     logger.info(message)
    # elif level == 'debug':
    #     logger.debug(message)
    # elif level == 'warning':
    #     logger.warning(message)
    # elif level == 'error':
    #     logger.error(message)

    return logger

    # logger.removeHandler(fh)
    # logger.removeHandler(ch)
    #
    # fh.close()
    # ch.close()






# logger().info('info message')












#
# logger('info','info message')
# logger('error','error message')
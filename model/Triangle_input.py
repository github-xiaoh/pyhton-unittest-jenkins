# -*- coding:utf-8 -*-

import re
import Triangle
from Triangle import compare


num = {}
test_num = {}
def Triangle_input_a(a):
    while True:
        if compare(a) != "请输入正整数或正小数":
            num['a'] = compare(a)
            break
        else:
            test_num['a'] = a
            # print('a:'+compare(a))
            break

def Triangle_input_b(b):
    while True:

        if compare(b) != "请输入正整数或正小数":
            num['b'] = compare(b)
            break
        else:
            test_num['b'] = b
            # print('b:'+compare(b))
            break

def Triangle_input_c(c):
    while True:

        if compare(c) != "请输入正整数或正小数":
            num['c'] = compare(c)
            break
        else:
            test_num['c'] = c
            # print('c:'+compare(c))
            break



# -*- coding:utf-8 -*-

import Triangle
from Triangle import compare
import Triangle_input



def Triangle_output(a,b,c):
    Triangle_input.Triangle_input_a(a)
    Triangle_input.Triangle_input_b(b)
    Triangle_input.Triangle_input_c(c)

    num = Triangle_input.num
    test_num = Triangle_input.test_num
    if compare(a) == "请输入正整数或正小数" or compare(b) == "请输入正整数或正小数" or compare(c) == "请输入正整数或正小数":
        # print(num)
        print("您输入的三个值分别为%s，%s，%s" % (a,b,c))
        print("您输入的三个值不符合要求：请输入正整数或正小数")
        return "输入值错误"

    else:
        print("您输入的三个值分别为%s，%s，%s" % (a, b, c))
        print("您输入的三个值组合结果为：")
        return Triangle.Triangle_PK(num['a'], num['b'], num['c'])





# a = input("输入组成三角形的第一个数：")
# b = input("输入组成三角形的第二个数：")
# c = input("输入组成三角形的第三个数：")
# Triangle_output(a,b,c)
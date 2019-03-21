# -*- coding:gb2312 -*-

import re
# import Triangle
import math


# def compare(a):
#     #调用正则
#     float_a = re.match(r'^[-+]?[0-9]+\.[0-9]+$',a)
#     if float_a or a.isdigit():
#         if float_a:
#             return float(a)
#         else:
#             return int(a)
#     else:
#         # print("请输入正整数或正小数")
#         return "请输入正整数或正小数"
#
#
#
# while True:
#     while True:
#         a =str(input("输入组成三角形的第一个数："))
#         if compare(a) != "请输入正整数或正小数":
#             break
#         else:
#             print(compare(a))
#     break




# print(type(L[1]))
    # if isinstance(i,int):
    #     print(int(i))
    # elif isinstance(i,float):
    #     print(float(i))




# print(isinstance(1.2,int))

# import re
# s= re.match("\d","adw")
# print (s,type(s))
# if str(s)=='None':
#     print (1)
# else:
#     print (2)


# def Triangle_input():
#     num = {}
#     while True:
#         while True:
#             a =input("输入组成三角形的第一个数：")
#             if compare(a) != "请输入正整数或正小数":
#                 num['a'] = compare(a)
#                 break
#             else:
#                 print(compare(a))
#         while True:
#             b =input("输入组成三角形的第二个数：")
#             if compare(b) != "请输入正整数或正小数":
#                 num['b'] = compare(b)
#                 break
#             else:
#                 print(compare(b))
#         while True:
#             c = input("输入组成三角形的第三个数：")
#             if compare(c) != "请输入正整数或正小数":
#                 num['c'] = compare(c)
#                 break
#             else:
#                 print(compare(c))
#         break
#
#
#     print("您输入的三个值分别为%s，%s，%s"%(num['a'],num['b'],num['c']))
#     print("您输入的三个值可组成：")
#     return Triangle.Triangle_PK(num['a'],num['b'],num['c'])


# def Triangle_input(a,b,c):
#     num = {}
#     while True:
#         while True:
#             # a =input("输入组成三角形的第一个数：")
#             if compare(a) != "请输入正整数或正小数":
#                 num['a'] = compare(a)
#                 break
#             else:
#                 num['a'] = a
#                 break
#         while True:
#             # b =input("输入组成三角形的第二个数：")
#             if compare(b) != "请输入正整数或正小数":
#                 num['b'] = compare(b)
#                 break
#             else:
#                 num['b'] = b
#                 break
#         while True:
#             # c = input("输入组成三角形的第三个数：")
#             if compare(c) != "请输入正整数或正小数":
#                 num['c'] = compare(c)
#                 break
#             else:
#                 num['c'] = c
#                 break
#         break
#
#     if compare(a)=="请输入正整数或正小数" or compare(b)=="请输入正整数或正小数" or compare(c)=="请输入正整数或正小数":
#         # print(num)
#         print("您输入的三个值分别为%s，%s，%s"%(num['a'],num['b'],num['c']))
#         print("您输入的三个值不符合要求：请输入正整数或正小数")
#         return '输入值错误'
#     else:
#         print("您输入的三个值分别为%s，%s，%s" % (num['a'], num['b'], num['c']))
#         print("您输入的三个值组合结果为：")
#         return Triangle.Triangle_PK(num['a'],num['b'],num['c'])


# Triangle_input('234trfgfd','鼎折覆?','2')

x = 8

print(math.sqrt(x))


try :

    open("ssd.txt",'r')
    print(sss)
    print(4+"dd")

except FileNotFoundError:
    print("\n")
    print( x)

except NameError:
    print("sdsdsdsd")

except:
    print("all")



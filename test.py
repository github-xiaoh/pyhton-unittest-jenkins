# -*- coding:gb2312 -*-

import re
# import Triangle
import math


# def compare(a):
#     #��������
#     float_a = re.match(r'^[-+]?[0-9]+\.[0-9]+$',a)
#     if float_a or a.isdigit():
#         if float_a:
#             return float(a)
#         else:
#             return int(a)
#     else:
#         # print("����������������С��")
#         return "����������������С��"
#
#
#
# while True:
#     while True:
#         a =str(input("������������εĵ�һ������"))
#         if compare(a) != "����������������С��":
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
#             a =input("������������εĵ�һ������")
#             if compare(a) != "����������������С��":
#                 num['a'] = compare(a)
#                 break
#             else:
#                 print(compare(a))
#         while True:
#             b =input("������������εĵڶ�������")
#             if compare(b) != "����������������С��":
#                 num['b'] = compare(b)
#                 break
#             else:
#                 print(compare(b))
#         while True:
#             c = input("������������εĵ���������")
#             if compare(c) != "����������������С��":
#                 num['c'] = compare(c)
#                 break
#             else:
#                 print(compare(c))
#         break
#
#
#     print("�����������ֵ�ֱ�Ϊ%s��%s��%s"%(num['a'],num['b'],num['c']))
#     print("�����������ֵ����ɣ�")
#     return Triangle.Triangle_PK(num['a'],num['b'],num['c'])


# def Triangle_input(a,b,c):
#     num = {}
#     while True:
#         while True:
#             # a =input("������������εĵ�һ������")
#             if compare(a) != "����������������С��":
#                 num['a'] = compare(a)
#                 break
#             else:
#                 num['a'] = a
#                 break
#         while True:
#             # b =input("������������εĵڶ�������")
#             if compare(b) != "����������������С��":
#                 num['b'] = compare(b)
#                 break
#             else:
#                 num['b'] = b
#                 break
#         while True:
#             # c = input("������������εĵ���������")
#             if compare(c) != "����������������С��":
#                 num['c'] = compare(c)
#                 break
#             else:
#                 num['c'] = c
#                 break
#         break
#
#     if compare(a)=="����������������С��" or compare(b)=="����������������С��" or compare(c)=="����������������С��":
#         # print(num)
#         print("�����������ֵ�ֱ�Ϊ%s��%s��%s"%(num['a'],num['b'],num['c']))
#         print("�����������ֵ������Ҫ������������������С��")
#         return '����ֵ����'
#     else:
#         print("�����������ֵ�ֱ�Ϊ%s��%s��%s" % (num['a'], num['b'], num['c']))
#         print("�����������ֵ��Ͻ��Ϊ��")
#         return Triangle.Triangle_PK(num['a'],num['b'],num['c'])


# Triangle_input('234trfgfd','���۸�?','2')

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



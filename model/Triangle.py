# -*- coding:utf-8 -*-


# 1、判断是否为三角形
'''1、a>0 or b>0 or c>0  2、a+b>c and a+c>b and b+c>a'''
# 2、判断是否为等腰三角形
'''1、'''
# 3、判断是否为等边三角形
# 4、判断代码判断是否正确


import re







Triangles = "普通三角形"
I_Triangles = "等腰三角形"
E_Triangles = "等边三角形"
R_Triangles = "直角三角形"
I_R_Triangles = "等腰直角三角形"
N_Triangles = "非三角形"


def Triangle(a,b,c):
    if a>0 and b>0 and c>0:
        if a+b>c and a+c>b and b+c>a:
            print(Triangles)
            return Triangles

        else:
            print(N_Triangles)
            return N_Triangles
    else:
        print("请输入三个正数")



def Triangle_PK(a,b,c):
    if a>0 and b>0 and c>0:
        if a + b > c and a + c > b and b + c > a:
            if a==b==c:
                print(E_Triangles)
                return E_Triangles
            elif a==b or b==c or a==c:
                if a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
                    print(I_R_Triangles)
                    return I_R_Triangles
                else:
                    print(I_Triangles)
                    return I_Triangles
            elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
                print(R_Triangles)
                return R_Triangles
            else:
                return Triangle(a,b,c)
        else:
            return Triangle(a,b,c)
    else:
        return Triangle(a,b,c)




def compare(x):
    #调用正则
    float_x = re.match(r'^[-+]?[0-9]+\.[0-9]+$',x)

    if float_x or x.isdigit():
        if float_x:
            return float(x)
        else:
            return int(x)
    else:
        # print("请输入正整数或正小数")
        return "请输入正整数或正小数"


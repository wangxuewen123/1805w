#!/usr/bin/env python
# coding=utf-8
#声明函数
def jisuan(a,b,c):
    if b == "*":
        suma = a*c
        print("乘法是%d"%suma)
    elif b == "/":
        suma = a/c
        print("除法是%d"%suma)
    elif b == "+":
        suma = a+c
        print("加法是%d"%suma)
    elif b == "-":
        suma = a-c
        print("减法是%d"%suma)
#调用函数
aa = int(input("请输入数字： "))
bb = input("请输入*/+-： ")
cc = int(input("请输入数字： "))
jisuan(aa,bb,cc)

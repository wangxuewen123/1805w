#!/usr/bin/env python
# coding=utf-8
def print_sun(shuzi):
    print(shuzi)
    suma = 0
    sumb = 0
    for i in range(shuzi+1):
        if i % 2 == 0:
            suma = suma+i
        else:
            sumb = sumb+i
    print("偶数和是%d"%suma)
    print("奇数和是%d"%sumb)
a = int(input("输入数字： "))
print_sun(a)

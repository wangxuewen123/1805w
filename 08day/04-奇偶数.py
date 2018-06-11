#!/usr/bin/env python
# coding=utf-8
kebian = int(input("请输入你要的数字： "))
a = 0
ouhe = 0
jihe = 0
zonghe = 0
while a <= kebian :#自己输入的数字
    zonghe += a#zonghe = zonghe + a
    if a % 2 == 0:
        print("偶数是%d"%a)
        ouhe += a
    else:
        print("奇数是%d"%a)
        jihe += a
    a += 1
print("偶数和是%d"%ouhe)
print("奇数和是%d"%jihe)
print("总和是%d"%zonghe)

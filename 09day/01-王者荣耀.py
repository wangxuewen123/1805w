#!/usr/bin/env python
# coding=utf-8
a = 0
while a < 3:
    c = input("请输入帐号： ")
    b = input("请输入密码： ")
    if c == '123'and b == '123':
        print("登录成功")
        mm = int(input("请选择0：法师 1：ADC 2：肉"))
        if mm == 0:
            print("妲姬")
        elif mm == 1:
            print("后裔")
        elif mm == 2:
            print("项羽")
        a = 3#终止循环 循环条件不成立停止循环
    else:
        print("输入有误")
    a+=1

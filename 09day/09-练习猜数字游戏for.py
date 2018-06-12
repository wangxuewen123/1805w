#!/usr/bin/env python
# coding=utf-8
import random
a = random.randint(1,100)
#for i in range(1,11):
b = 0
while True:
    b = b+1
    user = int(input("请输入你的数字： "))
    if user < 100:
        if user < a:
            print("猜小了")
        elif user > a:
            print("猜大了")
        elif user == a:
            print("猜对了")
            break
        else:
            print("输错了")
    else:
        print("只能是100以内的数字")

print("您一共猜了%d次"%b)

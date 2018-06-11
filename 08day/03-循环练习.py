#!/usr/bin/env python
# coding=utf-8
import random
suiji = random.randint(1,100)
a = 0
while a <= 10:
    user = int(input("请输入数字：  "))
    if user < suiji:
        print("猜小了")
    elif user > suiji:
        print("猜大了")
    else:
        break
        print("恭喜你猜对了，奖励你一个大嘴巴子")
    a += 1

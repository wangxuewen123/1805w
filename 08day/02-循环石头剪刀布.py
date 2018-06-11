#!/usr/bin/env python
# coding=utf-8
import random
while True:
    computer = random.randint(1,3)
    user = int(input("请输入  <1--石头 2--剪刀 3--布>:   "))#用户输入
    #电脑随机结果
    if computer == 1:
        print("美女机器人出了石头")
    elif computer == 2:
        print("美女机器人出了剪刀")
    elif computer == 3:
        print("美女机器人出了布")
    #用户
    if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        print("电脑弱爆了")
    elif user == computer:
        print("巧了 心有灵犀啊真是")
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        print("你好垃圾真菜哈哈哈哈～～～")
    else:
        print("没有这种出拳动作犯规了Git Out！！！")
    print("===============================================================================")
    print("不想玩请按0")
    if user == 0:
        print("退出成功")
        break
#-------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------


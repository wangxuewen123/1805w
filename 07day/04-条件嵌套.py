#!/usr/bin/env python
# coding=utf-8
game = input("请输入1,王者荣耀  2,植物僵尸  ")
account = "123"
passwd = "123"
if game == '1':
    while True:
        user = input("请输入帐号： ")
        passs = input("请输入密码： ")
        if user == account and passs == passwd:
            print("欢迎来到王者荣耀")
            xuanze = input("请选择你的英雄1--亚瑟 2--后裔 3--妲姬 4--凯 5--李白")
            if xuanze == '1':
                print("去上路")
            elif xuanze == "2":
                print("去下路")
            elif xuanze == '3':
                print("去中路")
            elif xuanze == '4':
                print("去辅助")
            elif xuanze == "5":
                print("去打野")
            else:
                print("其他英雄正在设计...............")
            break
        else:
            print("帐号或密码错误请重试")
elif game == "2":
    print("僵尸来了，请做好准备")
else:
    print("没有安装这个游戏")
#======================================啦啦啦拉拉=============================================
print("===========================哈哈哈===========================")
sex = input("请输入你的性别： ")
if sex == "男":
    a = int(input("请输入身高： "))
    b = int(input("请输入财富： "))
    c = int(input("请输入颜值： "))
    if a > 180 and b > 1000 and c > 90:
        print("高副帅")
    else:
        print("稳住别哭")
else:
    color = input("请输入皮肤颜色： ")
    caifu = int(input("请输入财富： "))
    yanzhi = int(input("请输入颜值： "))
    if color == '白色' and caifu > 800 and yanzhi > 90:
        print("百富没")
    else:
        print("哈哈哈")
print("==============================hahahaha================================")
#==================================分开==================================================
day = int(input("请输入今天星期几： "))
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    my = input("请输入上午还是下午？ ")
    if my == '上午':
        a = int(input("请输入时间： "))
        if a > 8 and a < 10:
            print("正在上课")
        elif a >= 10 and a < 12:
            print("玩游戏")
    if my == '下午':
        xiawu = input("请输入时间： ")
        if xiawu > "14" and xiawu < "5":
            print("正在上课")
        else:
            print("不知道在干嘛")
elif day == 6:
    print("全体上课")
elif day == 7:
    print("逛街")
else:
    print("一个星期只有7天")

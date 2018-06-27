#!/usr/bin/env python
# coding=utf-8
import time
#定义一个菜单
money = 0
def manue():
    print("欢迎来到自助小银行".center(50,"*"))
    print("1.添加账户".center(50," "))
    print("2.查询账户".center(50," "))
    print("3.存款".center(48," "))
    print("4.取款".center(48," "))
    print("5.修改账户".center(50," "))
    print("6.注销账户".center(50," "))
    print("7.退出系统".center(50," "))
#建一个可以存放账户的列表
lista = []
def add():
    print("请添加一个账户".center(50,"="))
    a = 0#写一个循环条件
    while a == 0:
        aa = input("确定添加一个新的帐号吗?\n确定输入\tY\n取消输入\tN\n>>>>>>>>>>>    ")
        if aa == "Y":
            #建一个字典保存信息,只显示每次添加的信息
            dic = {}
            while True:
                account = input("请输入新帐号(19位数字开头是6)： ")
                if len(account) <= 19 and account.startswith("6"):
                    break
                else:
                    print("输入格式错误！！！")
            while True:
                passwd = input("请输入密码(6位数数字密码)： ")
                if len(passwd) == 6:
                    break
                else:
                    print("输入格式错误！！！")
            while True:
                phone = input("请输入预留手机号(标准手机号11位数的)： ")
                if len(phone) == 11 and phone.startswith("1"):
                    dic1 = {"account":account,
                            "password":passwd,
                            "phone":phone}
                    dic.update(dic1)
                    lista.append(dic)#把新建的账户添加到上面的列表
                    break
                    #显示出来好看一点
                    print("添加成功".center(50,"$"))
                    print("帐号 --------%s\n密码 --------%s\n预留手机号 --%s\n>>>>>>>>>>>>>"%(dic["account"],dic["password"],dic["phone"]))
                else:
                    print("输入格式错误！！！")
            a = 1#条件不成立跳出循环
        elif aa == "N":
            a = 1#条件不成立跳出循环
        else:
            print("好好输入！！！")
def find():
    print("查看系统账户".center(50,"="))
    flag = 0#假设列表中没有任何东西
    for i in lista:
        if len(lista) >= 1:
            flag = 1
            print("帐号       >>> %s\n密码       >>> %s\n预留手机号 >>> %s"%(i["account"],i["password"],i["phone"]))
            print("金额       >>> %.2f\n>>>>>>>>>>>>>>>"%money)
    if flag == 0:
        print("提示：当前系统没有账户！")
#存款
def cun():
    print("存款￥".center(50,"="))
    flag = 0#写一个循环条件
    while flag == 0:
        me = input("请输入帐号： ")
        mima = input("请输入密码： ")
        for i in lista:
            if me == i["account"] and mima == i["password"]:
                cun1 = float(input("请输入存款金额： "))
                global money
                money = money+cun1
                print("您的金额为 %.2f元"%money)
                while True:
                    jixuqu = input("继续存款请输入Yes\t退出此功能请输入No\n>>>>>>>>>>>>>>  ")
                    if jixuqu == "Yes":
                        cun2 = float(input("请输入存款金额： "))
                        money = money+cun2
                    else:
                        print("退出成功    欢迎下次继续存款^_^")
                        break#跳出当前的这个循环
                flag = 1#跳出大循环
            else:
                print("帐号或密码输入错误请重试")
    print("您的金额为 %.2f"%money)
def qu():
    print("取款系统".center(50,"="))
    flag = 0
    while flag == 0:
        me = input("请输入帐号： ")
        mima = input("请输入密码： ")
        for i in lista:
            if me == i["account"] and mima == i["password"]:
                qu1 = float(input("请输入取款金额： "))
                global money
                if qu1 > money:
                    print("对不起！您的帐号中没钱啦......快去存！！！\n还有 %d元"%money)
                    cun()
                    #加入用户需求，如果存了一次没存够
                    print(".".center(50,"."))
                    q = float(input("请再次输入取款金额： "))
                    money = money-q
                    print("您的余额为 %.2f元"%money)
                    print("^^".center(50,"-"))
                money = money-qu1
                print("您的余额为 %.2f元"%money)
                print("^^".center(50,"-"))
                while True:
                    jixuqu = input("继续取款请输入Yes\t退出此功能请输入No\n>>>>>>>>>>>>>>  ")
                    if jixuqu == "Yes":
                        qu2 = float(input("请输入取款金额： "))
                        if qu2 > money:
                            print("您的金库没有钱！！！去存\n还有 %d元"%money)
                            cun()
                            qu3 = float(input("请输入取款金额： "))
                            money = money-qu3
                            print("您的余额为 %.2f"%money)
                        money = money-qu2
                        print("您的余额为 %.2f"%money)
                        print("^^".center(50,"-"))
                    else:
                        print("退出成功    欢迎下次继续取款^_^")
                        break
                flag = 1
            else:
                print("帐号或密码输入错误请重试\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("您的余额为 %.2f"%money)
#修改
def gai():
    print("修改账户信息".center(50,"="))
    a = 0
    while a == 0:
        me = input("请输入您要修改的帐号： ")
        for i in lista:
            if me == i["account"]:
                while True:
                    yan = input("为了您和他人的信息安全需要验证手机\n请输入您注册时候的预留手机号： ")
                    if yan == i["phone"]:
                        time.sleep(3)
                        print("正在验证中，请稍等...")
                        time.sleep(2)
                        print("正在检查手机号，wait Plase!!!....")
                        time.sleep(1)
                        print("验证成功")
                        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                        break
                    else:
                        time.sleep(3)
                        print("正在验证中，请稍等...")
                        time.sleep(2)
                        print("正在检查手机号，wait Plase!!!....")
                        time.sleep(1)
                        print("验证失败，请输入正确的预留手机号\n>>>>>>>>>>>>>>>>>>>>>>>>>")
                gai = int(input("修改帐号请输入1\t修改密码请输入2\t修改电话请输入3\n>>>>>>>>>>>>>  "))
                if gai == 1:
                    gai1 = input("请输入新帐号： ")
                    i["account"] = gai1
                    print("修改成功新的帐号是 %s"%i["account"])
                elif gai == 2:
                    gai2 = input("请输入新的密码： ")
                    i["password"] = gai2
                    print("修改成功新的密码为 %s"%i["password"])
                elif gai == 3:
                    gai3 = input("请输入新的预留电话： ")
                    i["phone"] = gai3
                    print("修改成功新的预留电话为 %s"%i["phone"])
                a = 1
            else:
                print("帐号输入错误！！！\n查看您注册的帐号信息请输入 1")
                bian = input(">>>>>>>>>>>> ")
                if bian == "1":
                    find()
#删除
def dell():
    print("注销账号".center(50,"="))
    a = 0
    while a == 0:
        me = input("请输入您要注销的帐号： ")
        for i in lista:
            if me == i["account"]:
                lista.pop(0)
                print("注销成功 欢迎下次继续使用\n查看系统有没有帐号输入1")
                while True:
                    kan = input(">>>>>>>>>>> ")
                    if kan == "1":
                        find()
                        break
                    else:
                        print("别乱输入，会炸的")
                a = 1
            else:
                print("帐号输入错误！！！")
#主运行
a = 0
while a == 0:
    if len(lista) <= 1:
        while True:
            manue()
            my = int(input("请输入您需要的服务： "))
            if my == 1:
                add()
            elif my == 2:
                find()
            elif my == 3:
                cun()
            elif my == 4:
                qu()
            elif my == 5:
                gai()
            elif my == 6:
                dell()
            elif my == 7:
                break
            else:
                print("别乱输入，会炸的！！！")
    else:
        print("不好意思,为了您的信息金额的安全只能一次对一个帐号进行操作.")

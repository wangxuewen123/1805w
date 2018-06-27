#!/usr/bin/env python
# coding=utf-8
#定义一个系统菜单
def mnue():
    print("1.添加名片".center(55," "))
    print("2.查看名片".center(55," "))
    print("3.修改名片".center(55," "))
    print("4.删除名片".center(55," "))
    print("5.退出系统".center(55," "))
#定义添加名片
list1 = []#建一个列表保存下面填写的信息
def add():
    print("添加您的名片".center(50,"="))
    #建一个保存信息的字典
    dic = {}
    name = input("请输入姓名： ")
    sex = input("请输入性别： ")
    age = input("请输入年龄： ")
    job = input("请输入公司： ")
    phone = input("请输入电话： ")
    dic["name"] = name
    dic["sex"] = sex
    dic["age"] = age
    dic["job"] = job
    dic["phone"] = phone
    #把字典追加进列表
    list1.append(dic)
    print("添加成功".center(50,"-"))
    #遍历一下，增强显示效果
    for i in list1:
        print("姓名 %s\n性别 %s\n年龄 %s\n公司 %s\n电话 %s\n>>>>>>>>>>>>"%(i["name"],i["sex"],i["age"],i["job"],i["phone"]))
#定义查看名片
def look():
    print("以下就是所有名片".center(50,"="))
    for i in list1:
        print("姓名 %s\n性别 %s\n年龄 %s\n公司 %s\n电话 %s\n>>>>>>>>>>>>"%(i["name"],i["sex"],i["age"],i["job"],i["phone"]))
#定义修改名片
def gai():
    print("修改名片".center(50,"="))
    me = input("请输入您要修改的名片： ")
    for i in list1:
        if me == i["name"]:
            xuan = int(input("请选择您要修改的选项\n1.修改姓名\n2.修改性别\n3.修改年龄\n4.修改公司\n5.修改电话\n>>>>>>>>>>>>>\n"))
            if xuan == 1:
                name = input("请输入新的姓名： ")
                i["name"] = name
                print("修改成功--新的姓名为 %s"%i["name"])
            elif xuan == 2:
                sex = input("请输入新的性别： ")
                i["sex"] = sex
                print("修改成功--新的性别为 %s"%i["sex"])
            elif xuan == 3:
                age = input("请输入新的年龄： ")
                i["age"] = age
                print("修改成功--新的年龄为 %s"%i["age"])
            elif xuan == 4:
                job = input("请输入新的公司： ")
                i["job"] = job
                print("修改成功--新的公司为 %s"%i["job"])
            elif xuan == 5:
                phone = input("请输入新的电话： ")
                i["phone"] = phone
#定义删除名片
#def del():
    pass
#定义退出
#def tuichu():

#主函数执行
while True:
    print("欢迎进入名片管理系统".center(50,"*"))
    mnue()
    me = int(input("请输入选项： "))
    if me == 1:
        add()
    elif me == 2:
        look()
    elif me == 3:
        gai()
    elif me == 4:
        pass
    elif me == 5:
        print("退出成功，欢迎您的使用")
        break

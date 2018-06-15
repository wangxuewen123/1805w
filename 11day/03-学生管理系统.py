#!/usr/bin/env python
# coding=utf-8
all_list=[]
while True:
    user=input("请选择你的操作\n1--添加学生\n2--删除学生\n3--查询\n4--修改\n0--退出\n>>>")
    if user=="1":
        name=input("请输入你要添加的学生姓名： ")
        all_list.append(name)
        print(all_list)
    elif user=="2":
        my=input("请输入你要删除的学生： ")
        if my in all_list:
            all_list.remove(my)
            print(all_list)
        else:
            print("没有此人")
    elif user=="3":
        ca=input("请输入你要查的姓名： ")
        if ca in all_list:
            print("索引是",(all_list.index(ca)))
        else:
            print("没有此人")
    elif user=="4":
        aa=input("请输入你要查找的姓名： ")
        if aa in all_list:
            cc=all_list.index(aa)
            ss=input("请输入新名字： ")
            all_list[cc]=ss
            print(all_list)
        else:
            print("没有这个鬼.....")
    elif user=="0":
        break
    


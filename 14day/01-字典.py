#!/usr/bin/env python
# coding=utf-8
dic={"姓名":"王学文",
     "年龄":18,
     "住址":"山西",
     "电话":1234564,
     "民族":"汉族"}
'''
print(dic)
#修改
a=input("请输入你要修改的内容： ")
b=input("请输入你要改为什么： ")
dic[a]=b
print(dic)
#添加
aa=input("请输入你要添加的内容： ")
bb=input("请输入你要添加的内容： ")
dic[aa]=bb
print(dic)
#删除
aaa=input("请输入你要删除的内容： ")
dic.pop(aaa)
print(dic)
#合并
dic1={"asd":13123131}
dic.update(dic1)
print(dic)
'''
#字典的遍历
for i in dic.keys():
    print(i)
for a in dic.values():
    print(a)
for j in dic.items():
    for c in j:
        print(c)

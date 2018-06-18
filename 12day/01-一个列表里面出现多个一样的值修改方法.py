#!/usr/bin/env python
# coding=utf-8
all_list=['asd','asdaa','qq','asd']
for b,a in enumerate(all_list):
    print(b,a)
for a,i in enumerate(all_list):
    if i==all_list[3]:
        bb=int(input("请输入素号： "))
        aa=input("请输入改为： ")
        all_list[bb]=aa
        break
print(all_list)

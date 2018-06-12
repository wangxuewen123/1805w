#!/usr/bin/env python
# coding=utf-8
a = 1
while a < 6:
    b = 0
    while b < a:
        b+=1
        print("*",end="")#end=""不希望换行打印
    print("") #换行
    a+=1

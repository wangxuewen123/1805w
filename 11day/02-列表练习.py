#!/usr/bin/env python
# coding=utf-8
listt=[]
b=0
for i in range(100,201):
    a = 0
    for j in range(2,i):
        if i%j == 0:
            a = 1
            break
    if a == 0:
        b=b+i
        listt.append(i)
print("素数是",listt )
print("素数和是%d"%b)
listt.sort()
listt.sort(reverse=True)
print("降序是",listt)
listt.reverse()
print("倒序是",listt)




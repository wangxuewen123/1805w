#!/usr/bin/env python
# coding=utf-8
def d_sum(a,b,*args,**kwargs):
    suma = a+b
    for b in args:
        print(b)
        suma = suma+b
    for i in kwargs.values():
        print(i)
        suma = suma+i
    return suma
t = (1,2,3,4,5,6)
d = {"age":12,"weight":24}
aaa = d_sum(1,2,*t,**d)
print(aaa)

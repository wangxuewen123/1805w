#!/usr/bin/env python
# coding=utf-8
lista=[1,2,3,4,5,6,7,8,9]
for i in range(len(lista)-1,-1,-1):
    lista.pop(i)
print(lista)

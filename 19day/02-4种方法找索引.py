#!/usr/bin/env python
# coding=utf-8
#第一种
lista = [1,100,49,10,56,3,2,37]
a = lista.index(3)
print("索引是%d"%a)
#第二种
a = 0
while a < len(lista):
    if lista[a] == 3:
        print("索引是%d"%a)
        break
    a += 1

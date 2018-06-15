#!/usr/bin/env python
# coding=utf-8
import random
all_liat=[]
a=1
while a<11:
    b=random.randint(1,100)
    if all_liat.count(b) < 1:
        all_liat.append(b)
    a+=1
if len(all_liat) == 10:
    print(all_liat)
else:
    b=random.randint(1,100)
    if all_liat.count(b) < 1:
        all_liat.append(b)
        print(all_liat)




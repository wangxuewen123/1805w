#!/usr/bin/env python
# coding=utf-8
for row in range(1,10):
    for hang in range(1,row+1):
        print("%d*%d=%d"%(hang,row,hang*row),end="\t")
        if row == hang:
            print("")
            break

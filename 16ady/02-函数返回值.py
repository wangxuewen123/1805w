#!/usr/bin/env python
# coding=utf-8
def sa(acc,pwd):
    if len(acc) == 11 and acc.startswith("1") and len(pwd) > 6:
        return True
    else:
        return False
aa = input("号： ")
bb = input("密码： ")
ww = sa(aa,bb)
if ww:
    print("OK")
else:
    print("NO")

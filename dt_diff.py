#!/usr/bin/env python3
# coding: UTF-8
# version 0.04
from datetime import date
from monthdelta import monthmod
dt1 = input("開始日は?: ")
dt2 = input("終了日は?: ")
def ymd(arg):
    y, m, d = int(arg[:4]),int(arg[4:6]),int(arg[-2:])
    a = date(y, m, d)
    return a
t1 = ymd(dt1)
if dt2 == "":
    t2 = date.today()
else:
    t2 = ymd(dt2)
dt_dif = abs(t1 - t2)
if t2 < t1:
    mmod_1 = monthmod(t2,t1)
else:
    mmod_1 = monthmod(t1,t2)
print(f'{dt_dif.days}日です')
if 1 <= mmod_1[0].months < 12:
    print(f'{mmod_1[0].months}月 {mmod_1[1].days}日です。')
elif mmod_1[0].months >= 12:
    y,m = divmod(mmod_1[0].months,12)
    print(f'{y}年 {m}月 {mmod_1[1].days}日です。')
else:
    print(f'{mmod_1[1].days}日です。')

#!/usr/bin/env python3
# coding: UTF-8
# version 0.03
import sys
import datetime
from monthdelta import monthmod
args = sys.argv
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
k = [line for line in lines_strip if args[-2] in line]
k1 = k[-1][1:11]
k2 = k[-2][1:11]
t1 = datetime.date.fromisoformat(k1)
t2 = datetime.date.fromisoformat(k2)
dt_dif = t1 - t2
mmod = monthmod(t2,t1)
print("{}日前です".format((dt_dif).days))
if 1 <= mmod[0].months < 12:
    print(f'{mmod[0].months}月 {mmod[1].days}日前です。')
elif mmod[0].months >= 12:
    y,m = divmod(mmod[0].months,12)
    print(f'{y}年 {m}月 {mmod[1].days}日前です。')
else:
    print(f'{mmod[1].days}日前です。')
print(k[-2])
print(k[-1])

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
kk = k[-1][1:11]
t1 = datetime.date.fromisoformat(kk)
ddn = datetime.date.today()
mmod = monthmod(t1,ddn)
print("{}日前です".format((ddn - t1).days))
if 1 <= mmod[0].months < 12:
    print(f'{mmod[0].months}月 {mmod[1].days}日前です。')
elif mmod[0].months >= 12:
    y,m = divmod(mmod[0].months,12)
    print(f'{y}年 {m}月 {mmod[1].days}日前です。')
# else:
#     print(f'{mmod[1].days}日前です。')
print(k[-1])

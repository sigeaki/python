#!/usr/bin/env python3
# coding: UTF-8
# version 0.04
import sys
import datetime
from monthdelta import monthmod
args = sys.argv
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
k = [line for line in lines_strip if args[-2] in line]
kk1 = k[-1][1:11]
kk2 = k[-2][1:11]
t1 = datetime.date.fromisoformat(kk1)
t2 = datetime.date.fromisoformat(kk2)
ddn = datetime.date.today()
mmod1 = monthmod(t1,ddn)
mmod2 = monthmod(t2,t1)
if 1 <= mmod1[0].months < 12:
    print(f'{args[-2]}は今日から{(ddn - t1).days}日、{mmod1[0].months:2}月{mmod1[1].days:2}日前です。')
elif mmod1[0].months >= 12:
    y,m = divmod(mmod1[0].months,12)
    print(f'{args[-2]}は今日から{(ddn - t1).days}日、{y:2}年{m:2}月{mmod1[1].days:2}日前です。')
else:
    print(f'{args[-2]}は今日から{(ddn - t1).days}日前です')
if 1 <= mmod2[0].months < 12:
    print(f'{args[-2]}は前回から{(t1 - t2).days}日、{mmod2[0].months:2}月{mmod2[1].days:2}日前です。')
elif mmod2[0].months >= 12:
    y,m = divmod(mmod2[0].months,12)
    print(f'{args[-2]}は前回から{(t1 - t2).days}日。{y:2}年{m:2}月{mmod1[1].days:2}日前です。')
else:
    print(f'{args[-2]}は前回から{(t1 - t2).days}日前です')
print(k[-2][:15])
print(k[-1][:15])

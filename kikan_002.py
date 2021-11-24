#!/usr/bin/env python3
# coding: UTF-8
# version 0.01
from datetime import date
from monthdelta import monthmod
dt = input("DAte?: ")
y, m, d = int(dt[:4]),int(dt[4:6]),int(dt[-2:])
t1 = date(y,m,d)
t2 = date.today()
dt_dif = t2 - t1
mmod = monthmod(t1,t2)
print("{}日前です".format((dt_dif).days))
if 1 <= mmod[0].months < 12:
    print(f'{mmod[0].months}月 {mmod[1].days}日前です。')
elif mmod[0].months >= 12:
    y,m = divmod(mmod[0].months,12)
    print(f'{y}年 {m}月 {mmod[1].days}日前です。')
else:
    print(f'{mmod[1].days}日前です。')

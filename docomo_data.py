#!/usr/bin/env python3
# coding: UTF-8
import datetime
import calendar
n=float(input("今日までのデータ使用量は？:"))
ddn=datetime.datetime.now()
d=ddn.day
m=ddn.month
nn=n/d
_, ld = calendar.monthrange(ddn.year,m)
print("{}日までの平均データ使用量は{:.2f}".format(d,nn))
print("{}月のデータ使用量の予定は{:.2f}".format(m,nn*ld))

#!/usr/bin/env python3
# coding: UTF-8
# version 0.01
import re
import sys
from datetime import timedelta
from datetime import date
args = sys.argv
df = lambda a:date.fromisoformat(a)
def youbi(x):
    day_list = [["Mon","(月)"],["Tue","(火)"],["Wed","(水)"],["Thu","(木)"],["Fri","(金)"],["Sat","(土)"],["Sun","(日)"]]
    for i in range(7):
        if x.strftime("%a") == day_list[i][0]:
            return day_list[i][1]
s_word = args[-2]
ddn = date.today()
with open(args[-1],'r') as f:
    k = [line[1:11] for line in f if s_word in line]
    kk = [df(k) for k in k[::-1]]
    kkk = [(kk[i]-kk[i+1]).days for i in range(len(kk)-1)]
y = kk[0]
print(f'前回は {y.strftime("%Y-%m-%d")}{youbi(y)}  {(ddn - kk[0]).days}日前です。')
print(f'平均間隔は {int(sum(kkk)/len(kkk)):,}日です。')
y += timedelta(sum(kkk)/len(kkk))
print(f'次回予定は {y.strftime("%Y-%m-%d")}{youbi(y)}です。')

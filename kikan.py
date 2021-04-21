#!/usr/bin/env python3
# coding: UTF-8
# version 0.01
import sys
import datetime
args = sys.argv
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
k = [line for line in lines_strip if args[-2] in line]
kk = k[-1][1:11]
t1 = ddn=datetime.date.fromisoformat(kk)
ddn = datetime.date.today()
kkk = ddn - t1
print("{}日前です".format(kkk.days))

#!/usr/bin/env python3
# coding: UTF-8
# version 0.03
import sys
import datetime
args = sys.argv
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
k = [line for line in lines_strip if args[-2] in line]
k1 = k[-1][1:11]
k2 = k[-2][1:11]
t1 = datetime.date.fromisoformat(k1)
t2 = datetime.date.fromisoformat(k2)
print("{}日前です".format((t1 - t2).days))
print(k[-2])
print(k[-1])

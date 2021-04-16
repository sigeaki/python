#!/usr/bin/env python3
# coding: UTF-8
# version 0.03
import re
import sys
import datetime
args = sys.argv
ddn=datetime.datetime.now()
if len(args) < 3:
    search_word = ddn.strftime("-%m-%d")
else:
    search_word = args[-2]
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
k = [(i,line) for i,line in enumerate(lines_strip) if re.search(search_word,line)]
for line in k:
    print("{}:{}".format(line[0],line[-1]))
t1 = k[-1][0]
t2 = k[-2][0] - 1
print(t1 - t2)
if args[1] == '-c':
    print('マッチ行数は{}回です'.format(len(k)))

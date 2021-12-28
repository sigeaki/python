#!/usr/bin/env python3
# coding: UTF-8
# version 0.02
import re
import sys
import datetime
args = sys.argv
if len(args) < 3:
    ddn=datetime.datetime.now()
    search_word = ddn.strftime("-%m-%d")
else:
    search_word = args[-2]
with open(args[-1],'r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
r_lines_strip = list(reversed(lines_strip))
k = [line for line in r_lines_strip if re.search(search_word,line)]
if len(k) > 21:
    kk = k[:21]
    for line in kk:
        print(line)
else:
    for line in k:
        print(line)
if args[1] == '-c':
    print('マッチ行数は{}行です'.format(len(k)))

#!/usr/bin/env python3
# coding: UTF-8
# version 0.04
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
    # lines = f.readlines()
# lines_strip = [line.strip() for line in lines]
# k = [line for line in lines_strip if re.search(search_word,line)]
    k = [line.replace("\n","")  for line in f if re.search(search_word,line)]
for line in k:
    print(line)
if args[1] == '-c':
    print('マッチ行数は{}回です'.format(len(k)))

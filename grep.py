#!/usr/bin/env python3
# coding: UTF-8
import re
import sys
import datetime
args = sys.argv
if len(args) < 2:
    ddn=datetime.datetime.now()
    search_word = ddn.strftime("-%m-%d")
else:
    search_word = args[1]
with open('/home/sigeaki/LL750share/howm/diary.txt','r') as f:
    lines = f.readlines()
lines_strip = [line.strip() for line in lines]
#k = [line for line in lines_strip if search_word in line]
k = [line for line in lines_strip if re.search(search_word,line)]
for line in k:
    print(line)

print('検索結果は{}回です'.format(len(k)))

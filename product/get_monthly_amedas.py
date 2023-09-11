#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import csv, os, re

for y in range(2001,2023):
    url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/monthly_a1.php?prec_no=14&block_no=1507&year=%d&month=3&day=01&view=p1'%y
    data = pd.read_html(url, header=0)
    data[0] = data[0].set_axis(['月','合計降水量','日最大降水量','最大１時間降水量','最大10分間降水量','日平均気温','日平均最高気温','日平均最低気温','最高気温','最低気温',\
                          '平均湿度','最小湿度','平均風速','最大風速','最大風向','最大瞬間風速','最大瞬間風向','日照時間','降雪の深さの合計','日降雪の深さの合計','最深積雪'],axis='columns')
    data[0].drop(columns=['最大１時間降水量','最大10分間降水量','平均湿度','最小湿度','最大瞬間風速','最大瞬間風向','降雪の深さの合計','日降雪の深さの合計','最深積雪'], inplace=True)
    data[0].drop(index=range(2),inplace=True)
    filename = str(y) + 'monthweather.csv'
    data[0].to_csv(filename,index = False,encoding='utf_8_sig')
    with open(filename, newline='',encoding='utf_8_sig') as f:
        reader = csv.reader(f)
        n_row = []
        for row in reader:
            temp = []
            for r in row:
                n_r = re.sub(r'(-?\d{,4}\.?\d?).+\)|\]',r'\1',str(r))
                # n_r = re.sub(r'(-?[0-9]{,3}\.\d).+\)?',r'\1',str(r))
                temp.append(n_r)
            n_row.append(temp)
    with open(filename, 'w',encoding='utf_8_sig') as f:
        writer = csv.writer(f)
        for item in n_row:
            writer.writerow(item)

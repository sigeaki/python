#!/usr/bin/env python3
# coding: utf-8
# version 0.15

import pandas as pd
import numpy as np
import datetime
import sys

args = sys.argv
dt_now = datetime.datetime.now()
dt_now_str_1 = f'{dt_now.year}年{dt_now.month}月{dt_now.day}日'
t = int(dt_now.hour)
print(dt_now_str_1)

response = pd.read_html('https://tenki.jp/amedas/1/2/14136.html', encoding='utf-8', index_col=1)
pd.options.display.float_format = '{:.1f}'.format
df = response[4].iloc[:t,1:6]
try:
    df = df.astype({'気温(℃)':'float','降水量(mm)':'float32','風速(m/s)':'float32','日照時間(分)':'int8'})
except:
    df.replace('---', np.nan, inplace=True)
    df = df.astype({'気温(℃)':'float','降水量(mm)':'float32','風速(m/s)':'float32'})
# sun_total, rain_total = df['日照時間(分)'].sum(), df['降水量(mm)'].sum() 
rain_total = df['降水量(mm)'].sum() 
print(df.describe()) # describe関数でとりあえず概要表示
print(df)
# print(f'合計日照時間は、{sun_total:.0f}分')
print(f'合計降水量は、{rain_total:.1f}mm')
if len(args) > 1 and args[1] == "-g":
    import matplotlib.pyplot as plt
    import japanize_matplotlib
    df.plot(y=['気温(℃)','風速(m/s)'], marker="o", markersize=4, grid=True)
    plt.show()

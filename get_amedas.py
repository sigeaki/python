#!/usr/bin/env python3
# coding: utf-8
# version 0.08

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import numpy as np
# import os

dt_now = datetime.datetime.now()

response = requests.get('https://weather.yahoo.co.jp/weather/amedas/1b/14136.html')
mat = []  # 保存先の行列
soup = BeautifulSoup(response.content, "html.parser")
# tableの取得
table = soup.find('table')

# trの解析
trs = table.find_all('tr')
# ヘッダーの解析
r = []  # 保存先の行
tr = trs[0]
for td in tr.find_all('td'):  # 1回目のtdタグを走査する
    r.append(td.text.strip())
mat.append(r[:-1])

# ボディの解析
for tr in trs[1:]:  # 最初の行を飛ばしてfor文で回す
    r = []  # 保存先の行
    for td in tr.find_all('td'):  # tdタグを走査する
        r.append(td.text.strip())
    mat.append(r[:-1])
dt_nor_str_1 = dt_now.strftime('%Y-%m-%d')
dt_nor_str_2 = f'{dt_now.year}年{dt_now.month}月{dt_now.day}日'

l = dt_now.hour + 2

m = []
for k in mat[:-1]:
    if len(k) > 6 and k[1] == '24時':
        k[1] = '0時'
        m.append(k[1:])
    if len(k) > 6:
        m.append(k[1:])
    else:
        m.append(k)
df = pd.DataFrame(data=m[1:l], columns=m[0])
try:
    df_int = df.astype({'気温（℃）':'float64','降水量（mm）':'float64','風速（m/s）':'float64','日照時間（分）':'int8'})
except:
    df.replace('---', np.NaN, inplace=True)
    df_int = df.astype({'気温（℃）':'float64','降水量（mm）':'float64','風速（m/s）':'float64','日照時間（分）':'int8'})
# hd = os.path.expanduser("~")

# if df_int.iloc[0,0] == '23時':
#     df_int.iloc[::-1].to_csv(hd + '/' + dt_nor_str_1 + "weather.csv",index = False,encoding='utf_8_sig')
# else:
df_temp_avg = df_int['気温（℃）'].mean()
df_rain_total = df_int['降水量（mm）'].sum()
df_wind_avg = df_int['風速（m/s）'].mean()
df_sun_total = df_int['日照時間（分）'].sum()
# print(df_int.iloc[::-1])
print(df_int)
print(f'{dt_nor_str_2}の平均気温は、{df_temp_avg:.1f}℃')
print(f'{dt_nor_str_2}の合計降水量は、{df_rain_total:,}mm')
print(f'{dt_nor_str_2}の平均風速は、{df_wind_avg:.1f}（m/s）')
print(f'{dt_nor_str_2}の合計日照時間は、{df_sun_total:,}分')

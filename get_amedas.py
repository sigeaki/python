#!/usr/bin/env python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import csv

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
print(dt_now.strftime('%Y-%m-%d'))

m = []
for k in mat[:-1]:
    if k[1] == '24時':
        break
    if len(k) > 6:
        m.append(k[1:])
    else:
        m.append(k)
df = pd.DataFrame(data=m[1:], columns=m[0])
print(df)

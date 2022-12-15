#!/usr/bin/env python3
# coding: utf-8
# version 0.01

import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def get_response(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def get_table(soup):
    mat = []  # 保存先の行列    
    # tableの取得
    table = soup.find('table')
    # trの解析
    trs = table.find_all('tr')
    # ヘッダーの解析
    r = []  # 保存先の行
    tr = trs[0]
    r = [ td.text for td in tr.find_all('th')]# thタグを走査する
    mat.append(r)
    # ボディの解析
    for tr in trs[1:]:  # 最初の行を飛ばしてfor文で回す
        r = []  # 保存先の行
        for td in tr.find_all('td'):  # tdタグを走査する
            r.append(td.text)
        mat.append(r)
    return mat

url_list = ["https://www.shogi.or.jp/game/record/all.html","https://www.shogi.or.jp/game/record/year_result.html"]
csv_list = ["all_result.csv","2022_result.csv"]
hd = os.path.expanduser("~") + '/'

for i in range(len(csv_list)):
    s = get_response(url_list[i])
    m = get_table(s)
    df = pd.DataFrame(m[1:],columns=m[0])
    df_sort = df.sort_values(by='勝率',ascending=False)
    df_sort.reset_index(drop=True, inplace=True) 
    df_sort.to_csv(hd  + csv_list[i],index = False, float_format='%4.4f')
    # print(df_sort)

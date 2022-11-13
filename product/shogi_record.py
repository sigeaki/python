#!/usr/bin/env python3
# coding: UTF-8
# version 0.01
import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
#現在時刻を取得
now = datetime.datetime.now()
hd = os.path.expanduser("~")
url_list = ["https://www.shogi.or.jp/game/record/all.html","https://www.shogi.or.jp/game/record/year_result.html"]
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
    # 出力
    # for item in mat:
    #     print(','.join(item))  # カンマ（,）で列を結合して表示
    csvFile = open(hd + "/" + now.strftime("%Y%m%d") + ".csv", 'at', newline='', encoding='utf_8_sig')
    writer = csv.writer(csvFile)
    for item in mat:
        writer.writerow(item)
    csvFile.close()
for u in url_list:
#    print(u)
    s = get_response(u)
    get_table(s)

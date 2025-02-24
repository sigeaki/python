#!/usr/bin/env python3
#"_FxPriceBoardMain__price_1hfca_33" coding: UTF-8
# version 0.02

import csv
import requests
from bs4 import BeautifulSoup
import re

# URLの指定
leage = 'j1', 'j2'
for j in leage:
    html = requests.get("https://www.jleague.jp/standings/" + j + "/")
    bsObj = BeautifulSoup(html.text, "html.parser")
    #print(bsObj)
    #更新日を取得
    update_time = bsObj.find(class_="standingsDate").text.strip()
    print(update_time)
    # テーブルを指定
    table = bsObj.find_all('tr')
    standing = []
    for row in table:
        tmp = []
        for item in row.find_all('td'):
            if item.a:
                tmp.append(item.text[0:len(item.text) // 2])
            else:
                tmp.append(item.text)
        del tmp[0]
        del tmp[-1]
        standing.append(tmp)
    for item in standing:
        print(item)
    r = re.sub(r'\D','-',update_time).lstrip('-')
    rr = r[:10].rstrip('-')
    csvFile = open(rr + j + ".csv", 'wt', newline='', encoding='utf_8_sig')
    writer = csv.writer(csvFile)
    for item in standing:
        writer.writerow(item)
    csvFile.close()
    with open(rr + j +  ".csv", 'a') as f:
        f.write(update_time)

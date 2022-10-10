#!/usr/bin/env python3
# coding: UTF-8
# version 0.04
import requests
from bs4 import BeautifulSoup
import datetime
from csv import writer
import os
#現在時刻を取得
t_delta = datetime.timedelta(hours=9)  # 9時間
JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
now = datetime.datetime.now(JST)
now_19 = "{0.year}-{0.month:2}-{0.day:2} {0.hour:2}:{0.minute:2}".format(now)
#米ドル/円サイトからデータを取得
url_list = [["https://finance.yahoo.co.jp/quote/USDJPY=FX","IL99C0xX","米ドル/円: "],\
                    ["https://finance.yahoo.co.jp/quote/EURJPY=FX","_3Pvw_N8d","ユーロ/円: "]]
yen_price = [now_19]
for i in range(len(url_list)):
    r = requests.get(url_list[i][0])
    soup = BeautifulSoup(r.text,"html.parser");
    yen_price.append(soup.find("span",class_=url_list[i][1]).text)
hd = os.path.expanduser("~")
with open(hd + '/yen_price.csv', 'a', newline='') as f_object:  
    writer_object = writer(f_object)
    writer_object.writerow(yen_price)  
    f_object.close()

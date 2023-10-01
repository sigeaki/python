#!/usr/bin/env python3
#"_FxPriceBoardMain__price_1hfca_33" coding: UTF-8
# version 0.04
import requests
from bs4 import BeautifulSoup
import datetime
from csv import writer
import os
#現在時刻を取得
now = datetime.datetime.now()
# now_day = "{0.year}-{0.month:2}-{0.day:2}".format(now)
now_day = now.strftime("%F")
# now_time = "{0.hour:2}:".format(now) + now.strftime("%M")
now_time = now.strftime("%H:%M")
#米ドル/円サイトからデータを取得
url_list = [["https://finance.yahoo.co.jp/quote/USDJPY=FX","_FxPriceBoardMain__price_1w4it_33","米ドル/円: "],\
                    ["https://finance.yahoo.co.jp/quote/EURJPY=FX","_FxPriceBoardMain__price_1w4it_33","ユーロ/円: "]]
yen_price = [now_day,now_time]
for i in range(len(url_list)):
    r = requests.get(url_list[i][0])
    soup = BeautifulSoup(r.text,"html.parser");
    yen_price.append(soup.find("span",class_=url_list[i][1]).text)
hd = os.path.expanduser("~")
with open(hd + '/yen_price.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(yen_price)
    f_object.close()

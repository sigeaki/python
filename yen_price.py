#!/usr/bin/env python3
#"_FxPriceBoardMain__price_1hfca_33" coding: UTF-8
# version 0.05
import requests
from bs4 import BeautifulSoup
import datetime
from csv import writer
import os
#現在時刻を取得
now = datetime.datetime.now()
now_day = now.strftime("%F")
now_time = now.strftime("%H:%M")
#米ドル/円サイトからデータを取得
url = 'https://finance.yahoo.co.jp/quote/USDJPY=FX'
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
yen_price = [now_day,now_time]

h3_tag = soup.find_all("h3", class_="_Heading_1t311_1 _FxRateItem__name_1ye8x_12")
h3_tag_text = []
for i in h3_tag:
    h3_tag_text.append(i.text)
price_list = soup.find_all("span",class_="_FxRateItem__number_1ye8x_48")
p_list = price_list[::2]
p_list_text = []
for i in p_list:
    p_list_text.append(i.text)
p_data = {h : p for h, p, in zip(h3_tag_text, p_list_text)}
price_list = [p_data['米ドル/円'],p_data['ユーロ/円']]
yen_price += price_list

hd = "/home/sigeaki/public/howm/price"
with open(hd + '/yen_price.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(yen_price)
    f_object.close()

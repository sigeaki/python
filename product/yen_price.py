#!/usr/bin/env python3
# version 0.06
import datetime
import yfinance as yf
from csv import writer
import os
#現在時刻を取得
now = datetime.datetime.now()
now_day = now.strftime("%F")
now_time = now.strftime("%H:%M")
yen_price = [now_day,now_time]
stock_tup = "USDJPY=X", 'EURJPY=X',#'CNYJPY=X'
ask_pid = []
# 米(ドル) / 日本(円)
for k in stock_tup:
    STOCK = yf.Ticker(k) 
    # .info取得
    STOCK_info = STOCK.info
    ask_pid += [STOCK_info['ask'],STOCK_info['bid']]
yen_price += ask_pid
hd = "/home/sigeaki/public/howm/price"
with open(hd + '/yen_price.csv', 'a', newline='') as f_object:
    writer_object = writer(f_object)
    writer_object.writerow(yen_price)
    f_object.close()

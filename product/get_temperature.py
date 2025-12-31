#!/usr/bin/env python3
# coding: utf-8

import requests
import json
import sys
import datetime
import time
import base64
import uuid
import hmac
import hashlib
import pandas as pd
import os
import csv
from pathlib import Path
import get_env

args = sys.argv
# wind direction
wd = { 0:"-", 1:"北北東", 2:"北東", 3:"東北東", 4:"東", 5:"東南東", 6:"南東", 7:"南南東", 8:"南", 9:"南南西", 10:"南西", 11:"西南西", 12:"西", 13:"西北西", 14:"北西", 15:"北北西", 16:"北" } 

# functions
def get_rdate():
  # date time now
    t_delta = datetime.timedelta(hours=9)  # 9時間
    JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
    dt_now = datetime.datetime.now(JST)
    gdate = dt_now + datetime.timedelta(minutes=-12)  # 現在時刻から12分引く
    gdate = gdate.strftime('%Y%m%d%H%M')              # 時刻を表す文字列に変換 
    return gdate[0:11] + "000"                        # 分の1の位と秒を0に

def dt2str(dt):
  return f"{dt[0:4]}-{dt[4:6]}-{dt[6:8]} {dt[8:10]}:{dt[10:12]}"

get_dt = get_rdate()
dt_str = dt2str( get_dt )
#print(get_dt, dt_str)

# get json
jdata = f"https://www.jma.go.jp/bosai/amedas/data/map/{get_dt}.json"
#jdata = "https://www.jma.go.jp/bosai/amedas/data/map/20230117050000.json"
#print(jdata)
dt_str_list = dt_str.split(' ')

df = requests.get(jdata).json()
#print(df['14136'])
# fields = ["時間", "気温", '日照時間', '降水量', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]
try:
    df_data1 = [df['14136']['temp'][0], df['14136']['sun1h'][0] * 60, df['14136']['precipitation1h'][0], wd[df['14136']['windDirection'][0]],  df['14136']['wind'][0]]
    fields = ["時間", "気温", '日照時間', '降水量', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]

except:
    df_data1 = [df['14136']['temp'][0], df['14136']['precipitation1h'][0], wd[df['14136']['windDirection'][0]],  df['14136']['wind'][0]]
    fields = ["時間", "気温", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]
    fields = ["時間", "気温", '降水量', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]

#現在時刻を取得
t_delta = datetime.timedelta(hours=9)  # 9時間
JST = datetime.timezone(t_delta, 'JST')  # UTCから9時間差の「JST」タイムゾーン
now = datetime.datetime.now(JST)

def make_apiheader():
    # Declare empty header dictionary
    apiHeader = {}
    # open token
    token = get_env.get_env('TOKEN')
    # secret key
    secret = get_env.get_env('SECRET')
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)
    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())

    #Build api header JSON
    apiHeader['Authorization']=token
    apiHeader['Content-Type']='application/json'
    apiHeader['charset']='utf8'
    apiHeader['t']=str(t)
    apiHeader['sign']=str(sign, 'utf-8')
    apiHeader['nonce']=str(nonce)
    return apiHeader
# API endpoint for getting device list
api_url = "https://api.switch-bot.com/v1.1/devices"
apiHeader= make_apiheader()
# Send GET request to the API
response = requests.get(api_url, headers=apiHeader)
device_id_list = ['F8B813BA77D8','DF8257D77F73']

df_data2 = []
for s in device_id_list:
    url = api_url + "/" + s + '/status'
    response = requests.get(url, headers=apiHeader)
    res=json.loads(response.text)
    temp, hum = res['body']['temperature'], res['body']['humidity']
    df_data2.append(temp)
    df_data2.append(hum)

row = dt_str_list[1:] + df_data1 + df_data2

if len(args) < 2:
    hd = os.path.expanduser("~")
    files = hd + "/public/howm/weather/" + dt_str_list[0] + 'temp.csv'
    if not Path(files).exists():
        with open(files,'w',  newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerow(row)
    else:
        with open(files, 'a', newline='', encoding='utf_8_sig') as f:
            writer = csv.writer(f)
            writer.writerow(row)
else:
    df = pd.DataFrame(row, index=fields)
    df.columns = [dt_str_list[0]]
    print(df)

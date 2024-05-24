#!/usr/bin/env python3
# coding: utf-8
# version 0.06

import requests
import json
import time
import hashlib
import hmac
import base64
import uuid
import sys
import datetime
from pathlib import Path
import csv
import os

# wind direction
wd = { 0:"-", 1:"北北東", 2:"北東", 3:"東北東", 4:"東", 5:"東南東", 6:"南東", 7:"南南東", 8:"南", 9:"南南西", 10:"南西", 11:"西南西", 12:"西", 13:"西北西", 14:"北西", 15:"北北西", 16:"北" } 

# functions
def get_rdate():
  # date time now
    dt_now = datetime.datetime.now()
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
# fields = ["時間", "気温", '日照時間(1h)', '降水量(ih)', "風向", "風速", "室温", "湿度"]
# fields = ["時間", "気温", '日照時間(1h)', '降水量(ih)', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]
fields = ["時間", "気温", '日照時間', '降水量', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]
df_data1 = [df['14136']['temp'][0], df['14136']['sun1h'][0] * 60, df['14136']['precipitation1h'][0], wd[df['14136']['windDirection'][0]],  df['14136']['wind'][0]]

#現在時刻を取得
now = datetime.datetime.now()

# Declare empty header dictionary
apiHeader = {}
# open token
token = 'ac13c69cd464914b76303eb915ab1f6903c0ba825c89742a2650271b9c825685b2be3552afbc3363719182d7a8b9c1d2' # copy and paste from the SwitchBot app V6.14 or later
# secret key
secret = '4a8fe0d45de9d100464d7ad5708903f6' # copy and paste from the SwitchBot app V6.14 or later
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

# API endpoint for getting device list
api_url = "https://api.switch-bot.com/v1.1/devices"

# Send GET request to the API
response = requests.get(api_url, headers=apiHeader)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    devices = response.json()
    device_id_list = [[device['deviceId'] for device in devices['body']['deviceList'] if "防水温湿度計 D8" in device['deviceName']],\
                  [device['deviceId'] for device in devices['body']['deviceList'] if "温湿度計 73" in device['deviceName']]]    
else:
    print("Failed to retrieve device list. Status Code:", response.status_code)
df_data2 = []
for i in range(2):
    url = "https://api.switch-bot.com/v1.1/devices/" + device_id_list[i][0] + '/status'
    response = requests.get(url, headers=apiHeader)
    res=json.loads(response.text)
    temp, hum = res['body']['temperature'], res['body']['humidity']
    df_data2.append(temp)
    df_data2.append(hum)
row = dt_str_list[1:] + df_data1 + df_data2
hd = os.path.expanduser("~")
files = hd + "/public/howm/weather/" + dt_str_list[0] + 'temp.csv'
# files = hd + "/" + dt_str_list[0] + 'temp.csv'
# print(Path(hd + "/" + dt_str_list[0] + 'temp.csv').exists())
#print(fl) 
if not Path(files).exists():
    with open(files,'w',  newline='', encoding='utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerow(row)
else:
    with open(files, 'a', newline='', encoding='utf_8_sig') as f:
        writer = csv.writer(f)
        writer.writerow(row)

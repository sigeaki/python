#!/usr/bin/env python3
# coding: utf-8
# version 0.02

import requests
import json
import sys
import datetime

#現在時刻を取得
now = datetime.datetime.now()

# functions
def get_rdate():
  # date time now
    dt_now = datetime.datetime.now()
    gdate = dt_now + datetime.timedelta(minutes=-12)  # 現在時刻から12分引く
    gdate = gdate.strftime('%Y%m%d%H%M')              # 時刻を表す文字列に変換
    return gdate[0:11] + "000"                        # 分の1の位と秒を0に

get_dt = get_rdate()
jdata = f"https://www.jma.go.jp/bosai/amedas/data/map/{get_dt}.json"
df = requests.get(jdata).json()
temp_out = df['14136']['temp'][0]
# Please get your access token via switchbot app
header = {"Authorization": "ac13c69cd464914b76303eb915ab1f6903c0ba825c89742a2650271b9c825685b2be3552afbc3363719182d7a8b9c1d2"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)

# Get deviceId for hygrometer of "your hygrometer device name" in all device information 
device_id = [device['deviceId'] for device in devices['body']['deviceList'] if "温湿度計 73" in device['deviceName']]

# call hygrometer state via switchbot api
url = "https://api.switch-bot.com/v1.0/devices/" + device_id[0] + '/status'
response = requests.get(url, headers=header)
res=json.loads(response.text)

print(now.strftime('%Y-%m-%d %H:%M'))
temp_in = res['body']['temperature']
humi = res['body']['humidity']
print(f'気温は{temp_out}℃')
print(f'室温は{temp_in}℃')
print(f'湿度は{humi}%')

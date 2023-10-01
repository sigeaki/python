#!/usr/bin/env python3
# coding: utf-8
# version 0.01

import requests
import json
import datetime

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
dt_str_list = dt_str.split(' ')

df = requests.get(jdata).json()
fields = ["時間", "気温", '日照時間(1h)', '降水量(ih)', "風向", "風速", "自宅外気温", "自宅外湿度", "室温", "湿度"]
df_data1 = [df['14136']['temp'][0], df['14136']['sun1h'][0], df['14136']['precipitation1h'][0], wd[df['14136']['windDirection'][0]],  df['14136']['wind'][0]]

#現在時刻を取得
now = datetime.datetime.now()

# Please get your access token via switchbot app
header = {"Authorization": "ac13c69cd464914b76303eb915ab1f6903c0ba825c89742a2650271b9c825685b2be3552afbc3363719182d7a8b9c1d2"}

# Get all device information in your switchbot hub
response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)
devices  = json.loads(response.text)
# Get deviceId for hygrometer of "your hygrometer device name" in all device information 
device_id_list = [[device['deviceId'] for device in devices['body']['deviceList'] if "防水温湿度計 D8" in device['deviceName']],\
                  [device['deviceId'] for device in devices['body']['deviceList'] if "温湿度計 73" in device['deviceName']]]
#print(device_id_list)
# call hygrometer state via switchbot api
df_data2 = []
for i in range(2):
    url = "https://api.switch-bot.com/v1.0/devices/" + device_id_list[i][0] + '/status'
    response = requests.get(url, headers=header)
    res=json.loads(response.text)
    temp, hum = res['body']['temperature'], res['body']['humidity']
    df_data2.append(temp)
    df_data2.append(hum)

row = dt_str_list[1:] + df_data1 + df_data2
print(dt_str_list[0])
print(fields)
print(row)


#!/usr/bin/env python3
# coding: UTF-8
# version 0.03

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import get_env

now = datetime.datetime.now()
tw = now + datetime.timedelta(days=1)
today = str(now.month) + '月' + str(now.day) + '日'
tomorrow = str(tw.month) + '月' + str(tw.day) + '日'

def GET_Weather():
    url = "https://tenki.jp/forecast/1/2/1400/1217/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    rs = soup.find(class_='forecast-days-wrap clearfix')
    # 天気を取得
    rs_wether = rs.findAll(class_='weather-telop')
    today_weather = rs_wether[0].text.strip()
    tomorrow_weather = rs_wether[1].text.strip()
    # 最高気温を取得
    rs_hightemp = rs.findAll(class_='high-temp temp')
    today_hightemp = rs_hightemp[0].text.strip().replace('\n', '')
    tomorrow_hightemp = rs_hightemp[1].text.strip()
    # 最高気温差を取得
    rs_hightempdiff = rs.findAll(class_='high-temp tempdiff')
    today_hightempdiff = rs_hightempdiff[0].text.strip()
    tomorrow_hightempdiff = rs_hightempdiff[1].text.strip()
    # 最低気温を取得
    rs_lowtemp = rs.findAll(class_='low-temp temp')
    today_lowtemp = rs_lowtemp[0].text.strip().replace('\n', '')
    tomorrow_lowtemp = rs_lowtemp[1].text.strip()
    # 最高気温差を取得
    rs_lowtempdiff = rs.findAll(class_='low-temp tempdiff')
    today_lowtempdiff = rs_lowtempdiff[0].text.strip()
    tomorrow_lowtempdiff = rs_lowtempdiff[1].text.strip()
    # 降水確率を取得
    rs_rain = soup.select('.rain-probability > td')
    today_rain_1 = rs_rain[0].text.strip()
    today_rain_2 = rs_rain[1].text.strip()
    today_rain_3 = rs_rain[2].text.strip()
    today_rain_4 = rs_rain[3].text.strip()
    tomorrow_rain_1 = rs_rain[4].text.strip()
    tomorrow_rain_2 = rs_rain[5].text.strip()
    tomorrow_rain_3 = rs_rain[6].text.strip()
    tomorrow_rain_4 = rs_rain[7].text.strip()
    # 風向
    rs_wind = soup.select('.wind-wave > td')
    #print(rs_wind)
    today_wind = rs_wind[0].text.strip()
    tomorrow_wind = rs_wind[1].text.strip()
    # 取得結果をdfに格納
    df = pd.DataFrame(
    data={now.strftime('%F'): ['天気', '最高気温', '最高気温差', '最低気温', '最低気温差',
            '降水確率[00-06]', '降水確率[06-12]', '降水確率[12-18]',
            '降水確率[18-24]', '風向'],
          today: [today_weather, today_hightemp, today_hightempdiff,
            today_lowtemp, today_lowtempdiff, today_rain_1, today_rain_2,
            today_rain_3, today_rain_4, today_wind],
          tomorrow: [tomorrow_weather, tomorrow_hightemp, tomorrow_hightempdiff,
            tomorrow_lowtemp, tomorrow_lowtempdiff, tomorrow_rain_1, tomorrow_rain_2,
            tomorrow_rain_3, tomorrow_rain_4, tomorrow_wind],
        }
    )
    return df

from_address = 'ssiiggeeaakkii@gmail.com'
to_address = 'ssiiggeeaakkii@gmail.com'
bcc = ''
# 発行したアプリパスワード
app_password = get_env.get_env('GMAIL_API')
subject = '天皇予報'
m = GET_Weather()
table_html = m.to_html(table_id="table",index=False)
body = f"""
    <html>
    </header>
    <body>
    {table_html}
    </html>
    """

def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
#    print(type(msg))
    return msg

def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587, timeout=15)
    smtpobj.starttls()
    smtpobj.login(from_address, app_password)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

message = create_message(from_address, to_address, bcc, subject, body)
send(from_address, to_address, message)

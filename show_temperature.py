#!/usr/bin/env python3
# coding: utf-8
# version 0.02

import pandas as pd
import sys

filename = sys.argv[1]
df = pd.read_csv(filename)
df['日照時間'] = df['日照時間'].astype('int')
print(df)
temp_ave, wave_ave, out_temp_ave, in_temp_ave = df['気温'].mean(), df['風速'].mean(), df['自宅外気温'].mean(), df['室温'].mean()
sun_total, rain_total = df['日照時間'].sum(), df['降水量'].sum() 
print(f'平均気温は、{temp_ave:.1f}℃')
print(f'合計日照時間は、{sun_total:.0f}分')
print(f'合計降水量は、{rain_total:.1f}mm')
print(f'平均風速は、{wave_ave:.1f}m/s')
print(f'自宅外平均気温は、{out_temp_ave:.1f}℃')
print(f'平均室温は、{in_temp_ave:.1f}℃')

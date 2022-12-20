#!/usr/bin/env python3
# coding: utf-8
# version 0.01

import sys
import pandas as pd
args = sys.argv

jyoken = input('抽出条件を入力してください:')
s_jyoken = input('ソート条件を入力してください:')
df = pd.read_csv(args[1],encoding='utf_8_sig',index_col=False)
for i in '勝数','負数':
    df[i] = df[i].dropna()#.apply(int).apply(str)
df_data = df.query(jyoken)
df_data.reset_index(drop=True, inplace=True)
d  = pd.DataFrame(df_data)
df_result = d.sort_values(by=s_jyoken,ascending=False)
df_result.reset_index(drop=True, inplace=True)
print(df_result)

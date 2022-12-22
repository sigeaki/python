#!/usr/bin/env python3
# coding: utf-8
# version 0.03

import sys
import pandas as pd
args = sys.argv

jyoken = input('抽出条件を入力してください:')
s_jyoken = input('ソート条件を入力してください:')
df = pd.read_csv(args[1],encoding='utf_8_sig',index_col=False)
df = df.fillna(0)
df = df.astype({'勝数': 'int64', '負数': 'int64'})
# for i in '勝数','負数':
#     df[i] = df[i].dropna()#.apply(int).apply(str)
df_data = df.query(jyoken)
df_data.reset_index(drop=True, inplace=True)
d  = pd.DataFrame(df_data)
df_result = d.sort_values(by=s_jyoken,ascending=False)
df_result.reset_index(drop=True, inplace=True)
for i in '対局数', '勝数', '負数':
    df_result[i] = df_result[i].apply(lambda x: '{0:,}'.format(x))
print(df_result)

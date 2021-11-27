#!/usr/bin/env python3
# coding: UTF-8
# version 0.02
# sysモジュールをインポート
import sys
from collections import Counter

args = sys.argv

if len(args) == 1 :
    print("正の整数を入力してください")
    sys.exit()

# args を整数型に変換
n = int(args[1])

# n が正の値でなければプログラムを終了
if n <= 0 :
    print("正の整数を入力してください")
    sys.exit()

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

r = Counter(factorize(n))
x = sorted(r.items())
j = []

if len(x) == 1:
    print("素数です",x[0][0])
else:
    for i in x:
        if i[1] == 1:
            y = i[0]
            j.append(y)
        else:
            j.append(i)
    print("合成数です",j)

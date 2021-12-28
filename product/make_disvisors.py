#!/usr/bin/env python3
# coding: UTF-8
# version 0.02

# sysモジュールをインポート
import sys
import datetime

args = sys.argv

# args を整数型に変換
if len(args) < 2:
    ddn=datetime.datetime.now()
    n = int(ddn.strftime("%Y%m%d"))
else:
    n = int(args[1])

# n が正の値でなければプログラムを終了
if n <= 0:
    print("正の整数を入力してください")
    sys.exit()

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

x = make_divisors(n)

if len(x) == 2:
    print(f'{x[1]}は素数です')
else:
    y = sum(x[:-1])
    if n == y:
        print(f'{x[-1]}は完全数です')
    elif n  > y:
        print(f'{x[-1]}は不足数です 約数は{x[:-1]}の{len(x)-2}個です 約数の合計は{y}です')
    elif n  < y:
        print(f'{x[-1]}は過剰数です 約数は{x[:-1]}の{len(x)-2}個です 約数の合計は{y}です')

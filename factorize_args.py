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

if len(x) == 1:
    print("素数です",x)
else:
    print("合成数です",x)

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
    print(f'{x[-1]}は合成数です 約数は{x[:-1]}です 約数の合計は{y}です')

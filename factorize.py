# sysモジュールをインポート
import sys

my_msg = "正の整数を入力してください："

# ユーザーが値を入力
n = input(my_msg)

# n を整数型に変換
n = int(n)

# n が正の値でなければプログラムを終了
if n <= 0:
    print(my_msg)
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

x = factorize(n)

if len(x) == 1:
    print("素数です",x)
else:
    print("合成数です",x)

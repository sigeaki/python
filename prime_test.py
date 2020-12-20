# 素数判定プログラム

# sysモジュールをインポート
import sys

my_msg = "正の整数を入力してください："

# ユーザーが値を入力
x = input(my_msg)

# x を整数型に変換
x = int(x)

# x が正の値でなければプログラムを終了
if x <= 0:
    print(my_msg)
    sys.exit()

# 除算の上限値を設定
ct = int(x**0.5)

for k in range(2, ct + 2):
# x が 1 または k で割り切れる場合
    if x == 1 or x % k == 0:
        print(x, "は素数ではありません。")
        break
else:
    print("{}は素数です".format(x))

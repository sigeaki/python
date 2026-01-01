#!/usr/bin/env python3
# coding: UTF-8
# version 0.02
import os
import requests
from bs4 import BeautifulSoup
# 出力先ディレクトリ
# output_dir = "./"
# 出力ファイル名
url = "https://ja.wikipedia.org/wiki/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
today = soup.find("div", attrs={"id": "on_this_day"}).text
hd = os.path.expanduser("~")
output_file = hd + "/output.txt"
# print(output_file)
with open(output_file, 'w+') as f:
    f.write(today)

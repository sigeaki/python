#!/usr/bin/env python3
# coding: UTF-8
# version 0.01
a = input("price? ")
r = [int(int(a) * 1.08)]
while True :
    a = input("price? ")
    if a == '=' :
        break
    b = int(int(a) * 1.08)
    r.append(b)
print(r,sum(r))

#!/usr/bin/env python3
# coding: UTF-8
# version 0.03
r = []
while (a := input("price? ")) != '':
    b = int(a)
    r.append(b)
print(f'price: {r} Total: {sum(r):,}')

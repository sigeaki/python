#!/usr/bin/env python3
# coding: UTF-8
# version 0.05
zeiritu = input("zeiritu?")
if zeiritu == '8':
    z = 8 
elif zeiritu == '10':
    z = 10
else:
    z = 0
def keisan(x):
    x = 1 + x / 100
    return x
r = []
a = input("price?:")
while a != '':
    r.append(int(a))
    a = input("price?:")
print(f'price: {r} Total: {sum(r):,} TaxTotal: {int(sum(r) * keisan(z)):,}')

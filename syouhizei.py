#!/usr/bin/env python3
# coding: UTF-8
# version 0.06
zeiritu = input("zeiritu? ")
if zeiritu == '8':
    z = 8 
elif zeiritu == '10':
    z = 10
else:
    z = 0
def keisan(x):
    return 1 + x / 100
r = []
a = input("price?: ")
while a != '':
    r.append(int(a))
    a = input("price?: ")
if z == 0:
    print(f'price: {r} Total: {sum(r):,}')
print(f'price: {r} Total: {sum(r):,} TaxTotal: {int(sum(r) * keisan(z)):,}')

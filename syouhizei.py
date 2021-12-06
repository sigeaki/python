#!/usr/bin/env python3
# coding: UTF-8
# version 0.07
def zeiritu(a):
    if a.lower() == 'k':
        return 8
    elif a.lower() == 'n':
        return 10
    else:
        return 0


def keisan(x):
    return 1 + x / 100


z = zeiritu(input("zeiritu? "))
r = []
a = input("price?: ")
while a != '':
    r.append(int(a))
    a = input("price?: ")
if z == 0:
    print(f'price: {r} Total: {sum(r):,}')
else:
    print(f'price: {r} Total: {sum(r):,} TaxTotal: {int(sum(r) * keisan(z)):,}')

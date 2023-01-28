# Problem: 强连通图
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4804/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf
if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


#       ms
def solve():
    n, m = RI()
    a, = RS()
    b, = RS()
    z = m * n
    dis = [[False] * z for _ in range(z)]
    for i in range(z):
        dis[i][i] = True
    for i, c in enumerate(a):
        if c == '>':
            for j in range(m - 1):
                u = i * m + j
                v = i * m + j + 1
                dis[u][v] = True
        else:
            for j in range(m - 1):
                v = i * m + j
                u = i * m + j + 1
                dis[u][v] = True

    for j, c in enumerate(b):
        if c == 'v':
            for i in range(n - 1):
                u = i * m + j
                v = (i + 1) * m + j
                dis[u][v] = True
        else:
            for i in range(n - 1):
                v = i * m + j
                u = (i + 1) * m + j
                dis[u][v] = True

    for k in range(z):
        for i in range(z):
            for j in range(z):
                if not dis[i][j] and dis[i][k] and dis[k][j]:
                    dis[i][j] = True
    # print(dis)
    for i in range(z):
        for j in range(z):
            if not dis[i][j]:
                return print('NO')
    print('YES')


if __name__ == '__main__':
    solve()

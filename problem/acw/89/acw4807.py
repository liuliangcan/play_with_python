# Problem: 构造矩阵
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4807/
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
    m, n = RI()
    b = []
    row, col = set(), set()
    for i in range(m):
        b.append(RILST())
        for j, v in enumerate(b[-1]):
            if v == 0:
                row.add(i)
                col.add(j)
    for i, r in enumerate(b):
        for j, v in enumerate(r):
            if v:
                if i in row and j in col:
                    return print('NO')
                if len(row) == m or len(col) == n:
                    return print('NO')
    a = [[1]*n for _ in range(m)]
    for i in row:
        a[i] = [0]*n
    for j in col:
        for i in range(m):
            a[i][j] = 0
    print('YES')
    for r in a:
        print(*r)


if __name__ == '__main__':
    solve()

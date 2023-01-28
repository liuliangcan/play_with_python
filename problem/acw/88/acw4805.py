# Problem: 金明的假期
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4805/
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
from math import sqrt, gcd, inf
# ACW没有comb
# from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


#    4330   ms
def solve1():
    n, = RI()
    a = RILST()
    f = [[inf] * 3 for _ in range(n)]  # 0/1/2 休息  看书 健身
    f[0][0] = 1
    if a[0] & 1:
        f[0][1] = 0
    if a[0] & 2:
        f[0][2] = 0

    for i in range(1, n):
        v = a[i]
        f[i][0] = min(f[i - 1]) + 1
        if v & 1:
            f[i][1] = min(f[i - 1][0], f[i - 1][2])
        if v & 2:
            f[i][2] = min(f[i - 1][0], f[i - 1][1])
    print(min(f[-1]))


#   4274     ms
def solve():
    n, = RI()
    a = RILST()
    y = z = inf  # 休息  看书 健身
    x = 0
    for v in a:
        x, y, z = min(x, y, z) + 1, min(x, z) if v & 1 else inf, min(x, y) if v & 2 else inf

    print(min(x, y, z))


if __name__ == '__main__':
    solve()

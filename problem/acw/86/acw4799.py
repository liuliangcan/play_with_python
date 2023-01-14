# Problem: 删除序列
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4799/
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
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


#       ms
def solve():
    n, = RI()
    a = RILST()
    mx = max(a)
    c = [0] * (mx + 1)
    for x in a:
        c[x] += 1
    f = [[0, 0] for _ in range(mx + 1)]
    for i in range(1, mx + 1):
        f[i][0] = max(f[i - 1])
        f[i][1] = f[i - 1][0] + i * c[i]

    print(max(f[-1]))


if __name__ == '__main__':
    solve()

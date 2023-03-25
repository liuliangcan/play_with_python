# Problem: 最大价值
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4880/
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
PROBLEM = """
"""


#       ms
def solve():
    n, m, v0, w0 = RI()
    f = [0] * (n + 1)
    for _ in range(m):
        l, h, v, w = RI()
        for j in range(n, -1, -1):
            for i in range(l // h + 1):
                vv = v * i
                if j >= vv:
                    f[j] = max(f[j], f[j - vv] + w * i)
    for j in range(v0, n + 1):
        f[j] = max(f[j], f[j - v0] + w0)
    print(max(f))


if __name__ == '__main__':
    solve()

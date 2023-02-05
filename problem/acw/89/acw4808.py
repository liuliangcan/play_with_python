# Problem: 加减乘
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4808/
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
    n, x, y = RI()
    f = [0] * (n + 1)
    for i in range(1, n + 1):
        f[i] = f[i - 1] + x
        if i & 1 == 0:
            f[i] = min(f[i], f[i // 2] + y)
        else:
            f[i] = min(f[i], f[(i + 1) // 2] + x + y)
    print(f[-1])


if __name__ == '__main__':
    solve()

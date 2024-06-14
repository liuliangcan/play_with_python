# Problem: P4377 [USACO18OPEN] Talent Show G
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P4377
# Memory Limit: 128 MB
# Time Limit: 1000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    n, w = RI()
    a = []
    for _ in range(n):
        x, y = RI()
        a.append((x, y * 1000))

    def ok(x):
        f = [0] + [-inf] * w
        for v, t in a:
            for j in range(w, -1, -1):
                p = min(w, j + v)
                f[p] = max(f[p], f[j] + t - x * v)
        return f[-1] <= 0

    l, r = sum(x for x, _ in a) / sum(y for _, y in a), max(y / x for x, y in a) + 1
    # for _ in range(60):
    while r - l > 1e-2:
        mid = (l + r) / 2
        if ok(mid):
            r = mid
        else:
            l = mid
    print(int(r))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

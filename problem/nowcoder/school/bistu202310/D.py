# Problem: 最长的递增矩阵序列
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/D
# Memory Limit: 524288 MB
# Time Limit: 4000 ms

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

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

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
PROBLEM = """LIS
容易想到分层按值域做DP转移，但是需要线段树优化，还得离散化，麻烦。
考虑把每层逆序，这样就排除了层内的影响。直接裸LIS
"""


#       ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        g.append(RILST())
    g = list(zip(*g))
    a = []
    for row in g:
        a.extend(sorted(row, reverse=True))
    f = []
    for v in a:
        if not f or v > f[-1]:
            f.append(v)
        else:
            f[bisect_left(f, v)] = v
    print(len(f))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

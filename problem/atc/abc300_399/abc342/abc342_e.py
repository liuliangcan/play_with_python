# Problem: E - Last Train
# Contest: AtCoder - HUAWEI Programming Contest 2024（AtCoder Beginner Contest 342）
# URL: https://atcoder.jp/contests/abc342/tasks/abc342_e
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""



#       ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        l, d, k, c, a, b = RI()
        a -= 1
        b -= 1
        g[b].append((a, l, d, k, c))  # 反图
    tt = [-inf] * n  # 从i走，最晚可以几点出发
    tt[-1] = inf
    q = [(-inf, n - 1)]  # 大顶堆取反

    while q:
        t, u = heappop(q)
        t = -t  # 大顶堆取反
        if t < tt[u]:  # dij
            continue
        for v, l, d, k, c in g[u]:
            if l + c > t:  # 最早走也到不了u
                continue
            last = min(l + (k - 1) * d, (t - c - l) // d * d + l)  # 要么最晚走，要么向下取整
            if last > tt[v]:  # 更优，那就再走一次
                tt[v] = last
                heappush(q, (-last, v))
    for v in tt[:-1]:
        if v > -inf:
            print(v)
        else:
            print('Unreachable')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

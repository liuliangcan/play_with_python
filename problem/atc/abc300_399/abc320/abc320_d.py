# Problem: D - Relative Position
# Contest: AtCoder - Toyota Programming Contest 2023#5（AtCoder Beginner Contest 320）
# URL: https://atcoder.jp/contests/abc320/tasks/abc320_d
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

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
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    n, m = RI()
    a = [(0, 0)] + [None] * (n - 1)
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, x, y = RI()
        g[u - 1].append((v - 1, x, y))
        g[v - 1].append((u - 1, -x, -y))
    vis = {0}
    q = deque([0])
    while q:
        u = q.popleft()
        ux, uy = a[u]
        for v, x, y in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                a[v] = (ux + x, uy + y)
    for ans in a:
        if ans:
            print(f"{ans[0]} {ans[1]}")
        else:
            print('undecidable')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

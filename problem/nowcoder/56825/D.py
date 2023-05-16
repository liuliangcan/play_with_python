# Problem: 遗迹探险
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/56825/D?&headNav=acm
# Memory Limit: 524288 MB
# Time Limit: 4000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """
"""
"""注意传送后宝藏重置，因此传送前和传送后的状态互不影响，可以看做两条单独的路径。
dp两次分别计算从起点到每个点的最大收益、从每个点到终点的最大收益
然后k方枚举跳跃即可。
"""

#       ms
def solve():
    n, m = RI()
    g = []  # 从起点到每个点的价值
    f = []  # 每个点到终点的价值
    for i in range(n):
        g.append(RILST())
        f.append(g[-1][:])
        for j in range(m):
            mx = i if i == j == 0 else -inf
            if i and g[i - 1][j] > mx:
                mx = g[i - 1][j]
            if j and g[i][j - 1] > mx:
                mx = g[i][j - 1]
            g[i][j] += mx
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            mx = 0 if i == n-1 and j == m-1 else -inf
            if i < n - 1 and f[i + 1][j] > mx:
                mx = f[i + 1][j]
            if j < m - 1 and f[i][j + 1] > mx:
                mx = f[i][j + 1]
            f[i][j] += mx
    t, = RI()
    for _ in range(t):
        k, = RI()
        port = []
        for _ in range(k):
            u, v = RI()
            port.append((u - 1, v - 1))

        ans = g[-1][-1]
        for u in range(k - 1):
            x, y = port[u]
            for v in range(u + 1, k):
                i, j = port[v]
                ans = max(ans, g[x][y] + f[i][j], g[i][j] + f[x][y])
        print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

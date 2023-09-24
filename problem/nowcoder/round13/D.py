# Problem: 小红的转账设置方式
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65507/D
# Memory Limit: 524288 MB
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

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""

def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    dis = [n] * n
    dis[0] = 0
    q = deque([0])
    while q:
        u = q.popleft()
        d = dis[u] + 1
        for v in g[u]:
            if d < dis[v]:
                dis[v] = d
                q.append(v)

    ans = 1
    for u, es in enumerate(g):  # 枚举每个点最短路
        p = 0
        for v in es:
            if dis[v] + 1 == dis[u]:  # u可以从v来
                p += 1
            elif dis[u] + 1 != dis[v] and u > v:  # 如果v从u来，则这条边去v里再计算；否则这条边不在最短路上，可以任意方向，但注意只计算一次
                ans = ans * 2 % MOD

        if p > 1:  # u有超过1条边来，那么只有全是反边的情况不可以
            ans = ans * (pow(2, p, MOD) - 1) % MOD

    print(sum(dis) % MOD, ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

# Problem: D. Lunar New Year and a Wander
# Contest: Codeforces - Codeforces Round 536 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1106/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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

if not sys.version.startswith('3.5.3'):  # ACW没有comb
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
PROBLEM = """https://codeforces.com/problemset/problem/1106/D

输入 n m(1≤n,m≤1e5) 和一个无向图的 m 条边。节点编号从 1 开始。
你从 1 出发，沿着边在图上行走，每遇到一个之前没有访问过的点，就把这个点的编号记录下来。你可以重复访问节点。
这个过程直到你记录了 n 个节点编号时停止。
输出这 n 个数的最小字典序。
输入
3 2
1 2
1 3
输出 1 2 3

输入
5 5
1 4
3 4
5 4
3 2
1 5
输出 1 4 3 2 5

输入
10 10
1 4
6 8
2 5
3 7
9 4
5 6
3 4
8 10
8 9
1 10
输出 1 4 3 7 9 8 6 5 2 10
"""
"""感觉可以用堆莽
"""


#       ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)

    ans = []
    q = [1]
    vis = [0] * (n + 1)
    vis[1] = 1
    while q:
        u = heappop(q)
        ans.append(u)
        for v in g[u]:
            if not vis[v]:
                vis[v] = 1
                heappush(q, v)
    print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

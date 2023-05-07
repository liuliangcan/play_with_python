# Problem: E. The Lakes
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/E
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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

MOD = 10 ** 9 + 7
PROBLEM = """
输入t组数据，每组数据：
输入n,m。
接下来输入n行，每行输入m个数，表示n×m的网格图g。
g[i][j]代表这个位置有深度为g[i][j]的水坑。水坑可以和上下左右四个相邻水坑相连。
问最大的一个连通坑的水体积。
"""
"""最大连通块点权"""
"""这题赛后竟然卡快读了，幸好我的板子直接快读"""
DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))


#       ms
def solve():
    m, n = RI()
    g = []
    for _ in range(m):
        g.append(RILST())

    def inside(x, y):
        return 0 <= x < m and 0 <= y < n

    def bfs(x, y):
        s = g[x][y]
        if not s:
            return 0
        g[x][y] = 0
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                a, b = x + dx, y + dy
                if inside(a, b) and g[a][b]:
                    s += g[a][b]
                    g[a][b] = 0
                    q.append((a, b))
        return s

    print(max(bfs(i, j) for i in range(m) for j in range(n)))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()

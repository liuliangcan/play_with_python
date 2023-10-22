# Problem: C - Sensors
# Contest: AtCoder - KEYENCE Programming Contest 2023 Autumn（AtCoder Beginner Contest 325）
# URL: https://atcoder.jp/contests/abc325/tasks/abc325_c
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    m, n = RI()
    g = []
    for _ in range(m):
        s, = RS()
        g.append([1 if c == '#' else 0 for c in s])

    def bfs(i, j):
        g[i][j] = 0
        q = deque([(i,j)])
        while q:
            x, y = q.popleft()
            for dx,dy in DIRS8:
                a, b = x +dx, y + dy
                if 0<=a<m and 0<=b<n and g[a][b]:
                    g[a][b] = 0
                    q.append((a, b))
    ans = 0
    for i in range(m):
        for j in range(n):
            if g[i][j]:
                ans += 1
                bfs(i,j)
    print(ans)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

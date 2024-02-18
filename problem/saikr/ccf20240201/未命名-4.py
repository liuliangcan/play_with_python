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
    m, n = RI()
    g = []
    for _ in range(n):
        g.append(RILST())
    gg = [[] for _ in range(n)]  # 给g顺时针转一下， 重力变成向左
    for j in range(n):
        for i in range(m - 1, -1, -1):
            gg[j].append(g[i][j])
    g = gg
    m, n = n, m
    vis = [[0] * n for _ in range(m)]
    time = 1

    def bfs(x, y):
        ans = []
        q = [(x, y)]
        v = g[x][y]
        vis[x][y] = time
        while q:
            nq = []
            for x, y in q:
                ans.append((x, y))
                for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                    if 0 <= a < m and 0 <= b < n and g[a][b] == v and vis[a][b] != time:
                        vis[a][b] = time
                        nq.append((a, b))
            q = nq
        return ans

    def dfs():
        nonlocal g
        gg = [v[:] for v in g]
        todo = []
        nonlocal time
        time += 1
        for i in range(m):
            for j in range(n):
                if not g[i][j]: break  # 重力是向左，这个位置没有，就可以看下一行
                if vis[i][j] != time:
                    q = bfs(i, j)
                    if len(q) >= 3:
                        todo.append(q)
        ans = 0
        for q in todo:
            for x, y in q:
                g[x][y] = 0

            for a in g:
                i = 0
                for v in a:
                    if v:
                        a[i] = v
                        i += 1
                for i in range(i, n):
                    a[i] = 0
            ans = max(ans, len(q) + dfs())
            g = [v[:] for v in gg]
        return ans

    print(dfs())


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

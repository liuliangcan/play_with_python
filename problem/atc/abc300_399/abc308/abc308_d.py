# Problem: D - Snuke Maze
# Contest: AtCoder - AtCoder Beginner Contest 308
# URL: https://atcoder.jp/contests/abc308/tasks/abc308_d
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
PROBLEM = """给出h行w列矩阵，每个位置是字母。
玩家从左上角走到右下角，沿路的字母组成的路径必须是'snuke'循环，问是否可以到达右下角。
"""
"""
显然转移的方向是按字母的，但是会循环。还是BFS比较方便，直接从左上角出发，向下一个字母转移即可。"""



#       ms
def solve():
    h, w = RI()
    g = []
    for _ in range(h):
        s, = RS()
        g.append(s)
    t = 'snuke'
    # if g[0][0] != 's' or g[-1][-1] != t[(h+w-1)%5]:
    if g[0][0] != 's':
        return print('No')
    dd = {}
    for i in range(1, len(t)):
        dd[t[i - 1]] = t[i]
    dd[t[-1]] = t[0]
    vis = [[0] * w for _ in range(h)]
    vis[0][0] = 1
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        c = g[x][y]
        d = dd[c]
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if 0 <= a < h and 0 <= b < w and not vis[a][b] and g[a][b] == d:
                if a == h-1 and b == w-1:
                    return print('Yes')
                vis[a][b] = 1
                q.append((a, b))
    # print(vis)
    print('No')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

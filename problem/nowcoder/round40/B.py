# Problem: 小红打怪
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/80259/B
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
    n, m = RI()
    g = []
    sx = sy = 0
    for i in range(n):
        s, = RS()
        g.append(s)
        for j, c in enumerate(s):
            if c in 'WASD':
                sx = i
                sy = j
    i,j = sx,sy
    ans = 0
    if g[i][j] == 'W':
        dx,dy = -1,0
    elif g[i][j] == 'S':
        dx,dy = 1,0
    elif g[i][j] == 'A':
        dx,dy = 0,-1
    elif g[i][j] == 'D':
        dx,dy = 0,1
    while 0<=i<n and 0<=j<m:
        if g[i][j] == '*':
            ans += 1
        i,j = i+dx,j+dy
    print(ans)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

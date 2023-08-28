# Problem: 小美的01串翻转
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/63869/C
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


#       ms
def solve():
    s, = RS()
    n = len(s)

    ans = 0
    for l in range(n):
        x = y = 0
        if s[l] == '1':
            x = 1
        else:
            y = 1
        for r in range(l + 1, n):
            if s[r] == '1':
                x, y = y + 1, x
            else:
                x, y = y, x + 1
            ans += min(x, y)
    print(ans)


#       ms
def solve1():
    s, = RS()
    n = len(s)
    f = [[0, 0] for _ in range(n)]
    ans = 0
    for l in range(n):
        f[l] = [0, 0]
        f[l][int(s[l]) ^ 1] = 1
        for r in range(l + 1, n):
            if s[r] == '1':
                f[r] = [f[r - 1][1] + 1, f[r - 1][0]]
            else:
                f[r] = [f[r - 1][1], f[r - 1][0] + 1]
            ans += min(f[r])
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

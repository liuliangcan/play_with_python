# Problem: F - Beautiful Path
# Contest: AtCoder - Japan Registry Services (JPRS) Programming Contest 2023 (AtCoder Beginner Contest 324)
# URL: https://atcoder.jp/contests/abc324/tasks/abc324_f
# Memory Limit: 1024 MB
# Time Limit: 5000 ms

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
PROBLEM = """https://blog.csdn.net/kksleric/article/details/7526239
0-1数分规划
"""


#       ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, b, c = RI()
        g[u].append((v, b, c))

    def ok(x):
        f = [-inf] * (n + 1)
        f[1] = 0
        for u in range(1, n + 1):
            if f[u] == -inf:
                continue
            for v, b, c in g[u]:
                f[v] = max(f[v], f[u] + b - x * c)
        return f[-1] < 0

    l, r = 0, 10 ** 4
    while r - l > 10 ** -10:
        mid = (l + r) / 2
        if ok(mid):
            r = mid
        else:
            l = mid
    print(r)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

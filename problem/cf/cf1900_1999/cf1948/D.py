# Problem: D. Tandem Repeats?
# Contest: Codeforces - Educational Codeforces Round 163 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1948/problem/D
# Memory Limit: 256 MB
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
    s, = RS()
    n = len(s)
    lcp = LCP1(s)
    for d in range(n // 2, 0, -1):
        for i in range(n - d):
            if lcp.lcp[i][i+d] >= d:
                return print(d*2)
    print(0)
def solve1():
    s, = RS()
    n = len(s)
    f = [0] * (n + 1)
    for d in range(n // 2, 0, -1):
        for i in range(n - d):
            if s[i] == s[i + d] or s[i] == '?' or s[i + d] == '?':
                f[i + 1] = f[i] + 1
                if f[i + 1] == d:
                    return print(d * 2)
            else:
                f[i + 1] = 0
    print(0)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

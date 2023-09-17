# Problem: C - Dice Sum
# Contest: AtCoder - UNIQUE VISION Programming Contest 2022（AtCoder Beginner Contest 248）
# URL: https://atcoder.jp/contests/abc248/tasks/abc248_c
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
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc248/tasks/abc248_c

输入 n m(1≤n,m≤50) k(n≤k≤n*m)。
输出有多少个长为 n 的数组 a 满足 1≤a[i]≤m 且 sum(a)≤k。
模 998244353。

数据加强版
输入 2 3 4
输出 6

输入 31 41 592
输出 798416518
"""
"""
f[i][j]长为i和为m的数组数量
"""


#     112   ms
def solve():
    n, m, k = RI()
    f = [0] * (k + 1)
    f[0] = 1
    for i in range(1, n + 1):
        pre = [0] + list(accumulate(f))
        f = [0] * (k + 1)
        for j in range(i, min(k, i * m) + 1):
            f[j] = (pre[j-1 + 1] - pre[j-min(m, j)]) % MOD

    print(sum(f) % MOD)


#       ms
def solve2():
    n, m, k = RI()
    f = [0] * (k + 1)
    f[0] = 1
    for i in range(1, n + 1):
        g = [0] * (k + 1)
        for j in range(min(k, i * m), i - 1, -1):
            for p in range(1, min(m, j) + 1):
                g[j] = (g[j] + f[j - p]) % MOD
        f = g
    print(sum(f) % MOD)


#   124    ms
def solve1():
    n, m, k = RI()
    f = [[0] * (k + 1) for _ in range(n + 1)]
    f[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i, min(k, i * m) + 1):
            for p in range(1, min(m, j) + 1):
                f[i][j] = (f[i][j] + f[i - 1][j - p]) % MOD
    print(sum(f[-1]) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

# Problem: Compatible Numbers
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/CF165E
# Memory Limit: 250 MB
# Time Limit: 4000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/165/e
https://www.luogu.com.cn/problem/CF165E
有两个整数a,b。如果a&b=0，那么我们称a与b是相容的。比如90(1011010)与36(100100)相容。给出一个序列a ，你的任务是对于每个ai，找到在序列中与之相容的aj 。如果找不到这样的数，输出-1。 贡献者：An_Account
输入n，(1<=n<=1e6) 
输入a(1<=a[i]<=4e6)
"""
"""f[x] 代表 对于数值x(x不一定在a里)，f[x]是x的一个相容数(f[x]一定在a里)
如果b是a的相容数(即f[a]=b)，存在c，c是a去掉一些1得到的，那么b一定也是c的相容数(f[c]=b)。
状态可以按上述转移。
这题上限4e6，22位，因此INF=(1<<22)-1。
我们要从INF开始向下遍历，对于每个数字x，如果这位是0，尝试补1后的数是否有相容数，如果有则继承过来。
因此f要开一个很大的数组记录每一个数的相容数。
"""


#    MLE    ms
def solve1():
    n, = RI()
    a = RILST()
    INF = (1 << 22) - 1
    f = {}
    for x in a:
        f[(x ^ INF) & INF] = x
    for x in range(INF - 1, 0, -1):
        if x not in f:
            for j in range(22):
                if not (x >> j) & 1:
                    p = x | (1 << j)
                    if p in f:
                        f[x] = f[p]
                        break
    print(*[f.get(x, -1) for x in a])


#    2276    ms
def solve():
    n, = RI()
    a = RILST()
    INF = (1 << 22) - 1
    f = [-1] * (INF + 1)
    for x in a:
        f[(x ^ INF) & INF] = x
    for x in range(INF - 1, 0, -1):
        if f[x] == -1:
            for j in range(22):
                if not (x >> j) & 1:
                    p = f[x | (1 << j)]
                    if p != -1:
                        f[x] = p
                        break
    print(*[f[x] for x in a])


#   2026     ms
def solve2():
    n, = RI()
    a = RILST()
    INF = (1 << 22) - 1
    f = [-1] * (INF + 1)
    for x in a:
        f[(x ^ INF) & INF] = x
    for x in range(INF - 1, 0, -1):
        if f[x] == -1:
            for j in range(22):
                if not (x >> j) & 1:
                    p = x | (1 << j)
                    if f[p] != -1:
                        f[x] = f[p]
                        break
    print(*[f[x] for x in a])


if __name__ == '__main__':
    solve()

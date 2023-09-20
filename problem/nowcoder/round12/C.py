# Problem: 小美的游戏
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65051/C
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
import random
from operator import iadd, imul
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
PROBLEM = """在乘积固定的情况下，使两个数和大，那么就尽量把因子放到一个数上，即把a*b变成1*(a*b)。
那么把k个大数都挪到最大的数上即可。
"""


#    432   ms
def solve():
    n, k = RI()
    a = RILST()
    a.sort(reverse=True)
    print((reduce(lambda x, y: x * y % MOD, a[:k + 1]) % MOD + k + sum(a[k + 1:]) % MOD) % MOD)


#    452   ms
def solve1():
    n, k = RI()
    a = RILST()
    a.sort(reverse=True)
    print((reduce(imul, a[:k + 1]) % MOD + k + sum(a[k + 1:]) % MOD) % MOD)


#    441   ms
def solve2():
    n, k = RI()
    a = RILST()
    a.sort(reverse=True)
    for i in range(1, k + 1):
        a[0] = a[0] * a[i] % MOD
        a[i] = 1
    print(sum(a) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

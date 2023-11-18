# Problem: F - Colored Ball
# Contest: AtCoder - Ｓｋｙ Inc, Programming Contest 2023（AtCoder Beginner Contest 329）
# URL: https://atcoder.jp/contests/abc329/tasks/abc329_f
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

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
PROBLEM = """
"""


#    379    ms
def solve():
    n, q = RI()
    c = [0] + RILST()
    cc = [{v} for v in c]

    for _ in range(q):
        a, b = RI()
        if len(cc[a]) > len(cc[b]):
            cc[a], cc[b] = cc[b], cc[a]
        cc[b] |= cc[a]
        cc[a] = set()
        print(len(cc[b]))


#     499   ms
def solve1():
    n, q = RI()
    c = [0] + RILST()
    cc = [{v} for v in c]

    for _ in range(q):
        a, b = RI()
        if len(cc[a]) < len(cc[b]):
            for v in cc[a]:
                cc[b].add(v)
            cc[a] = set()
        else:
            for v in cc[b]:
                cc[a].add(v)
            cc[b] = cc[a]
            cc[a] = set()
        print(len(cc[b]))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

# Problem: 小苯的台灯
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/A
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
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """只有4个状态，那么最多按3次就应该变，可以暴力
另外感觉可以打表
"""
ans = [[0] * 4] + [[-1] * 4 for _ in range(3)]
for n in range(1, 4):
    for k in range(4):
        p = n
        for i in range(1, 4):
            p = (p + k) % 4
            if p == 0:
                ans[n][k] = i
                break


#       ms
def solve():
    n, k = RI()
    print(ans[n][k % 4])


#   504    ms
def solve1():
    n, k = RI()
    if n == 0:
        return print(0)
    for i in range(1, 4):
        n = (n + k) % 4
        if n == 0:
            return print(i)
    print(-1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

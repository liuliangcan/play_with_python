# Problem: 408之计算机网络
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/E
# Memory Limit: 524288 MB
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
PROBLEM = """
"""


def f(s):
    ans = 0
    for v in map(int, s.split('.')):
        ans = ans << 8 | v
    return ans


def g(p, k):
    k = 32 - k
    p >>= k
    p <<= k
    ans = []
    m = (1 << 8) - 1
    for _ in range(4):
        ans.append(p & m)
        p >>= 8
    return '.'.join(map(str, ans[::-1]))


#       ms
def solve():
    n, = RI()
    k = 32
    s, = RS()
    p = f(s)
    for _ in range(n - 1):
        s, = RS()
        q = f(s)
        for i in range(k+1):
            if (p >> (32-i)) != (q >> (32-i)):
                k = i-1
                break

    print(f"{g(p, k)}/{k}")


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

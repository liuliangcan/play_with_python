# Problem: 可乐
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/16037
# Memory Limit: 2 MB
# Time Limit: 16037000 ms

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
"""答案是贪心的，一定是取一个可乐全买它
由于求字典序最大，那么找最后一个期望值最大的可乐
"""


#       ms
def solve():
    n, m, k = RI()
    mx, mxi = -inf, 0
    for i in range(k):
        x, y = RI()
        if x * m + y * (n - m) >= mx:
            mx = x * m + y * (n - m)
            mxi = i
    ans = [0] * k
    ans[mxi] = n
    print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

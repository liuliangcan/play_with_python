# Problem: F - Vouchers
# Contest: AtCoder - AtCoder Beginner Contest 308
# URL: https://atcoder.jp/contests/abc308/tasks/abc308_f
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
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """你要买n个物品，价格分别是pi.
你有m张满L减D的优惠券，每张券只能用一次。
问最少花多少钱可以买完这n个物品。
"""
"""贪心。
考虑双指针贪心，从大头开始还是小头。
发现大头不好贪。
从价格低物品开始买，考虑它能用哪张优惠券，选减得最多那个。这张券给更贵的不如给它用。
那么双指针+堆维护当前能用的券里最优那张即可。
"""


#  贪     ms
def solve():
    n, m = RI()
    p = RILST()
    l = RILST()
    d = RILST()
    p.sort()
    a = sorted(zip(l, d))
    h = []
    j = 0
    ans = 0
    for v in p:
        while j < m and a[j][0] <= v:
            heappush(h, -a[j][1])
            j += 1
        ans += v
        if h:
            ans += heappop(h)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

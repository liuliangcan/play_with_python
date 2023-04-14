# Problem: E - Kth Takoyaki Set
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_e
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_e
输入n(<=10),k(<=1e5),然后输入长度为n的数组a(1<=a[i]<=1e9)，a[i]代表第i种章鱼烧的价格。
每种章鱼烧可以取任意个，你可以选任意个章鱼烧组合起来计算总价，请问能组合成的第k小总价是多少。
"""
"""跟超级丑数一个套路，用小顶堆模拟，每次用堆顶的最小值拿出来，和每种价格组合一下入堆。注意记录vis数组。
"""


#       ms
def solve():
    n, k = RI()
    a = RILST()
    a.sort()
    h = [0]
    p = {0}
    for i in range(k):
        x = heappop(h)
        for v in a:
            c = x + v
            if c not in p:
                p.add(c)
                heappush(h, c)
    print(heappop(h))


if __name__ == '__main__':
    solve()

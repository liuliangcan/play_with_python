# Problem: Subarray Removal
# Contest: CodeChef - START89B
# URL: https://www.codechef.com/START89B/problems/REMSUBARR
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """给你一个1~n的排列，让你删除其中一段，剩下的数还是一个1~x的排列。
"""
"""显然是删除一个恰好涵盖x+1~n的段，那么从n开始往小了数，左右边界正好是数的个数即可"""

#       ms
# def solve():
#     n, = RI()
#     a = RILST()
#     st = SparseTable(a)
#     idx = {v: i for i, v in enumerate(a)}
#     ans = 1
#
#     for v in range(1, n + 1):
#         l, r = idx[v], n-1
#         if l > r:
#             l, r = r, l
#         if n - st.query(l, r) + 1 == r - l + 1 :
#             ans = max(ans,r - l + 1)
#     print(ans)
def solve():
    n, = RI()
    a = RILST()
    idx = {v: i for i, v in enumerate(a)}
    ans = 0
    l = n
    r = 0
    for i in range(n, 1, -1):
        pos = idx[i]
        l = min(l, pos)
        r = max(r, pos)
        if r - l == n - i:
            ans = r - l + 1
    print(ans)

if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

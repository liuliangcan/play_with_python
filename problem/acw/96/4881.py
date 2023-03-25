# Problem: 维护数组
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4881/
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

MOD = 10 ** 9 + 7
PROBLEM = """
"""


class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def set_point_min(self, i, v):  # 单点修改，
        self.add_point(i, v - self.a[i])
        self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s


#       ms
def solve():
    n, k, a, b, q = RI()
    d = [0] * (n + 1)
    treea = BinIndexTree(n + 1)
    treeb = BinIndexTree(n + 1)
    ans = []
    for _ in range(q):
        op, *z = RI()
        if op == 1:
            x, y = z
            d[x] += y
            treea.set_point_min(x, min(d[x], a))
            treeb.set_point_min(x, min(d[x], b))
        else:
            p = z[0]
            ans.append(treeb.sum_prefix(p - 1) + treea.sum_interval(p + k, n))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()

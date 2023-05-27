# Problem: Maximum Sum Permutation
# Contest: CodeChef - START91C
# URL: https://www.codechef.com/START91C/problems/MAXSUMPERM
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """
"""


class BinIndexTreeRUPQ:
    """树状数组的RUPQ模型，结合差分理解"""

    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def sum_prefix(self, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和
        s = 0
        while i >= 1:
            s += self.c[i]
            i &= i - 1
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(l, v)
        self.add_point(r + 1, -v)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(i)

    def lowbit(self, x):
        return x & -x


class Diff:
    def __init__(self, a):
        self.n = len(a)
        self.a = a[:]
        self.diff = diff = [a[0]] + [0] * self.n
        for i in range(1, self.n):
            diff[i] = a[i] - a[i - 1]

    def add(self, l, r, v):
        self.diff[l] += v
        self.diff[r + 1] -= v

    def update(self):
        return list(accumulate(self.diff[:-1]))


#       ms
def solve():
    n, q = RI()
    a = RILST()
    a.sort()
    d = Diff([0] * n)
    for _ in range(q):
        l, r = RI()
        d.add(l - 1, r - 1, 1)
    cnt = d.update()

    order = []

    x = 0
    ans = [0] * n
    for i in sorted(range(n), key=lambda b: -cnt[b]):
        ans[i] = a.pop()
        x += ans[i] * cnt[i]
    print(x)
    print(*ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

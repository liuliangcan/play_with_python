# Problem: G. Anya and the Mysterious String
# Contest: Codeforces - Codeforces Round 903 (Div. 3)
# URL: https://codeforces.com/contest/1881/problem/G
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
        return self.sum_prefix(i) % 26

    def lowbit(self, x):
        return x & -x


#       ms
def solve():
    n, m = RI()
    s, = RS()

    bit = BinIndexTreeRUPQ(n)
    for i, v in enumerate(s, start=1):
        bit.add_interval(i, i, ord(v))

    class IntervalTreeRURQSum:
        """区间加，区间求和"""

        def __init__(self, size):
            self.size = size
            self.interval_tree = [0 for _ in range(size * 4)]
            # self.lazys = [0 for _ in range(size * 4)]
            self.build(1, 1, size)

        def build(self, p, l, r):
            tree = self.interval_tree
            if l == r:
                tree[p] = 1

                # if l == 1:
                #     print(tree[p])
                return
            mid = (l + r) // 2
            self.build(p << 1, l, mid)
            self.build(p << 1 | 1, mid + 1, r)
            self.update_from_son(p, l, r)

        def update_from_son(self, p, l, r):
            tree = self.interval_tree
            if not tree[p << 1] or not tree[p << 1 | 1]:
                tree[p] = 0
                return
            mid = (l + r) // 2
            b, c = bit.query_point(mid), bit.query_point(mid + 1)
            if b == c:
                tree[p] = 0
                return
            if l < mid:
                a = bit.query_point(mid - 1)
                if a == c:
                    tree[p] = 0
                    return
            if mid + 1 < r:
                d = bit.query_point(mid + 2)
                if b == d:
                    tree[p] = 0
                    return
            tree[p] = 1

        # def give_lay_to_son(self, p, l, r):
        #     interval_tree = self.interval_tree
        #     lazys = self.lazys
        #     if lazys[p] == 0:
        #         return
        #     mid = (l + r) // 2
        #     interval_tree[p * 2] += lazys[p] * (mid - l + 1)
        #     interval_tree[p * 2 + 1] += lazys[p] * (r - mid)
        #     lazys[p * 2] += lazys[p]
        #     lazys[p * 2 + 1] += lazys[p]
        #     lazys[p] = 0

        def add_interval(self, p, l, r, x, y):
            """
            把[x,y]区域全修改
            """
            if y < l or r < x:
                return
            interval_tree = self.interval_tree
            # lazys = self.lazys
            if x <= l and r <= y:
                # interval_tree[p] += val * (r - l + 1)
                # lazys[p] += val
                return
            # self.give_lay_to_son(p, l, r)
            mid = (l + r) // 2

            if x <= mid:
                self.add_interval(p * 2, l, mid, x, y)
            if mid < y:
                self.add_interval(p * 2 + 1, mid + 1, r, x, y)
            self.update_from_son(p, l, r)

        def sum_interval(self, p, l, r, x, y):
            if y < l or r < x:
                return 1
            if x <= l and r <= y:
                # if l == r and x==y==1:
                #     print(p,x,y,l,r,self.interval_tree[p])
                return self.interval_tree[p]

            mid = (l + r) // 2

            if x <= mid:
                z = self.sum_interval(p * 2, l, mid, x, y)
                if not mid < y or not z:
                    return z
            if mid < y:
                z = self.sum_interval(p * 2 + 1, mid + 1, r, x, y)
                if not x <= mid or not z:
                    return z
            b, c = bit.query_point(mid), bit.query_point(mid + 1)
            if b == c:
                return 0
            if l < mid and x < mid:
                a = bit.query_point(mid - 1)
                if a == c:
                    return 0
            if mid + 1 < r and mid + 1 < y:
                d = bit.query_point(mid + 2)
                if b == d:
                    return 0

            return 1

    tree = IntervalTreeRURQSum(n)
    # print(tree.sum_interval(1, 1, n, 1, 1))
    for _ in range(m):
        t, *op = RI()
        if t == 1:
            l, r, x = op
            bit.add_interval(l, r, x)
            tree.add_interval(1, 1, n, l, r)
        else:
            l, r = op
            print(['NO', 'YES'][tree.sum_interval(1, 1, n, l, r)])


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://www.luogu.com.cn/problem/P3372
模板题，区间加，区间求和。
"""


class BinIndexTreeRURQ:
    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            i += -i&i

    def sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            i -= -i&i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(self.c, l, v)
        self.add_point(self.c, r + 1, -v)
        self.add_point(self.c2, l, (l-1)*v)
        self.add_point(self.c2, r + 1, -v*r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self.sum_prefix(self.c, r) * r - self.sum_prefix(self.c2, r) - self.sum_prefix(self.c, l - 1) * (
                l - 1) + self.sum_prefix(self.c2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(self.c, i)

    def lowbit(self, x):
        return x & -x


#  	 ms
def solve(n, m, a, qs):
    tree = BinIndexTreeRURQ(a)
    ans = []
    for q in qs:
        if q[0] == 1:
            l, r, x = q[1], q[2], q[3]
            tree.add_interval(l, r, x)
        elif q[0] == 2:
            l, r = q[1], q[2]
            ans.append(tree.sum_interval(l, r))
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    n, m = RI()
    a = RILST()
    q = []
    for _ in range(m):
        q.append(RILST())
    solve(n, m, a, q)

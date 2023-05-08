# Problem: C. LuoTianyi and the Show
# Contest: Codeforces - Codeforces Round 872 (Div. 2)
# URL: https://codeforces.com/contest/1825/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """输入t表示t组数据，每组：
输入n,m
接下来输入n个人的位置x[i]
-2 表示这个人只会坐到目前最右边人的右边紧挨着，若没人则坐0，若m有人就不坐离开。
-1 表示这个人只会坐到目前最左边人的左边紧挨着，若没人则坐m，若0有人就不坐离开。
正数x表示这个人会坐到位置x上，若有人就离开。
一共有m个座位，
你可以任意安排这些人的入场顺序，计算最多能做多少个人。
"""
"""
预处理x数组分为三类:-1,-2,正数
若没有正数，另外两类显然是互斥的，计算最大值即可（不能超过m
否则枚举第一个入场的正数，尝试从他开始左边和右边能放多少个，注意已存在正数的位置不用放，那么两边填空位即可。
第一个入场的正数x会使-1直接从x-1开始向左，那么还需要额外考虑-1从m开始的情况，可以看做第一个正数是m+1。但实际其实就是len(正数)+cnt[-1]。
同样考虑-2从1开始向右的情况。
"""



class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            # self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        # self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s

    def min_right(self, i):
        """寻找[i,size]闭区间上第一个正数(不为0的数),注意i是1-indexed。若没有返回size+1"""
        p = self.sum_prefix(i)
        if i == 1:
            if p > 0:
                return i
        else:
            if p > self.sum_prefix(i - 1):
                return i

        l, r = i, self.size + 1
        while l + 1 < r:
            mid = (l + r) >> 1
            if self.sum_prefix(mid) > p:
                r = mid
            else:
                l = mid
        return r

    def lowbit(self, x):
        return x & -x


#   342     ms
def solve1():
    n, m = RI()
    x = RILST()

    cnt = Counter(x)
    s = {v for v in x if v > 0}
    if not s:
        return print(min(max(cnt[-1], cnt[-2]), m))
    tree = BinIndexTree(m)
    for v in s:
        tree.add_point(v, 1)
    p = len(s)
    ans = max(p + cnt[-1], p + cnt[-2])
    for v in s:
        l = min(cnt[-1], v - 1 - tree.sum_prefix(v - 1))
        r = min(cnt[-2], m - v - tree.sum_interval(v + 1, m))
        ans = max(ans, p + r + l)
        if ans >= m:
            return print(m)

    print(ans)


#     358   ms
def solve():
    n, m = RI()
    x = RILST()

    cnt = Counter(x)
    s = {v for v in x if v > 0}
    x, y = cnt[-1], cnt[-2]
    if not s:
        return print(min(max(x, y), m))
    s = sorted(s)
    p = len(s)
    ans = max(p + x, p + y)
    for i, v in enumerate(s):
        l = min(x, v - 1 - i)
        r = min(y, m - v - (p - i - 1))
        ans = max(ans, p + r + l)
        if ans >= m:
            return print(m)

    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()

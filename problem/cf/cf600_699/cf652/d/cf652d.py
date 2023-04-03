# Problem: D. Nested Segments
# Contest: Codeforces - Educational Codeforces Round 10
# URL: https://codeforces.com/problemset/problem/652/D
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
PROBLEM = """https://codeforces.com/problemset/problem/652/D

输入 n(≤2e5) 和 n 个闭区间，区间左右端点范围在 [-1e9,1e9]，所有端点互不相同。

对每个区间，输出它包含多少个其它的区间。
输入
4
1 8
2 3
4 7
5 6
输出
3
0
1
0

输入
3
3 4
1 5
2 6
输出
0
1
1
"""


class SortedList:
    """简易SortedList名次树，只支持add不支持remove；所有操作复杂度<=log"""

    def __init__(self, a=None):
        self.small = []
        self.big = [] if not a else a

    def add(self, v):
        # 2000 1294ms
        # 1000 1216ms
        # 1500 1185ms
        # 1250 1232ms
        if len(self.small) > 1500:
            self.big += self.small
            self.big.sort()
            self.small.clear()
        insort(self.small, v)

    def __len__(self):
        return len(self.small) + len(self.big)

    def bisect_left(self, v):
        return bisect_left(self.small, v) + bisect_left(self.big, v)

    def bisect_right(self, v):
        return bisect_right(self.small, v) + bisect_right(self.big, v)

    def __contains__(self, v):
        p = bisect_left(self.small, v)
        if p < len(self.small) and self.small[p] == v:
            return True
        p = bisect_left(self.big, v)
        return p < len(self.big) and self.big[p] == v

    def __getitem__(self, index):
        if index < 0:
            index = len(self.small) + len(self.big) - index
        assert 0 <= index < len(self.small) + len(self.big)

        def findKthSortedArrays(nums1, nums2, k: int) -> int:
            index1, index2 = 0, 0
            m, n = len(nums1), len(nums2)
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        return findKthSortedArrays(self.small, self.big, index + 1)


#   SortedList  不离散化   1185ms
def solve():
    n, = RI()
    a = []
    for i in range(n):
        l, r = RI()
        a.append((r, l, i))
    a.sort()
    p = SortedList()
    ans = [0] * n
    for r, l, i in a:
        ans[i] = len(p) - p.bisect_left(l)
        p.add(l)
    print(*ans, sep='\n')


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

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s

    def lowbit(self, x):
        return x & -x


#    BIT 1185   ms
def solve2():
    n, = RI()
    a = []
    hs = []
    for i in range(n):
        l, r = RI()
        hs.extend([l, r])
        a.append((r, l, i))
    a.sort()
    hs.sort()
    ans = [0] * n
    n *= 2
    p = BinIndexTree(n)
    for r, l, i in a:
        l = bisect_left(hs, l)
        ans[i] = p.sum_interval(l + 1, n + 1)
        p.add_point(l + 1, 1)

    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()

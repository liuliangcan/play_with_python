# Problem: B. Mike and Feet
# Contest: Codeforces - Codeforces Round #305 (Div. 1)
# URL: https://codeforces.com/problemset/problem/547/B
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
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/547/B

输入 n(n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。
定义 f(x) 为 a 中「长为 x 的连续子数组的最小值」的最大值。
输出 f(1), f(2), ..., f(n)。
输入
10
1 2 3 4 5 4 3 2 1 6
输出
6 4 4 3 3 2 2 1 1 1 
"""


class MonoStack:
    # 单调栈，计算每个数作为最大/最小值值能到的前后边界。时/空复杂度O(n)
    # 注意，这里每个方法前/后遇到相同值的情况都是相反的，
    # 如果需要真实的前后边界，需要使用get_true的方法/或者调用两个函数，然后一边取l,一边取r
    def __init__(self, a):
        self.a = a

    def get_bound_as_max_left_over_and_right_stop(self):
        """使用单调递减栈，计算
        每个值作为最大值，前后能到达的边界（寻找左右第一个比它小的值）
        这里向左会越过相同值，向右会在相同值停下来。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] <= v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_bound_as_max_left_stop_and_right_over(self):
        """使用单调递减栈，计算
        每个值作为最大值，前后能到达的边界（寻找左右第一个比它小的值）
        这里向左会遇到相同值停下，向右会越过相同值。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] < v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_true_bound_as_max(self):
        # 使用单调递减栈，计算两边的真实边界(越过相同值)
        l, _ = self.get_bound_as_max_left_over_and_right_stop()
        _, r = self.get_bound_as_max_left_stop_and_right_over()
        return l, r

    def get_bound_as_min_left_over_and_right_stop(self):
        """使用单调递增栈，计算
        每个值作为最小值，前后能到达的边界（寻找左右第一个比它大的值）
        这里向左会越过相同值，向右会在相同值停下来。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] >= v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_bound_as_min_left_stop_and_right_over(self):
        """使用单调递增栈，计算
        每个值作为最小值，前后能到达的边界（寻找左右第一个比它大的值）
        这里向左会遇到相同值停下，向右会越过相同值。（防止重复计算区间）
        初始值为-1/n。
        """
        a, n = self.a, len(self.a)
        l, r, st = [-1] * n, [n] * n, []
        for i, v in enumerate(a):
            while st and a[st[-1]] > v:
                r[st.pop()] = i
            if st:
                l[i] = st[-1]
            st.append(i)
        return l, r

    def get_true_bound_as_min(self):
        # 使用单调递增栈，计算两边的真实边界(越过相同值)
        l, _ = self.get_bound_as_min_left_over_and_right_stop()
        _, r = self.get_bound_as_min_left_stop_and_right_over()
        return l, r


class BinIndexTreeMax:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数组；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.h = [-inf for _ in range(self.size + 5)]
            self.a = [-inf for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.a = [-inf for _ in range(self.size + 5)]
            self.h = [-inf for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.set_point(i + 1, v)

    def set_point(self, x, v):  # 单点修改，下标从1开始 修改原数组和h数组
        self.a[x] = v
        while x <= self.size:
            # self.h[x] = max(self.h[x], self.a[lx])
            if self.h[x] < v:
                self.h[x] = v
            x += (x & -x)

    def query_interval_max(self, l, r):  # 区间询问最大值，下标从1开始
        ans = -inf
        while l <= r:
            # ans = max(self.a[r], ans)
            if ans < self.a[r]:
                ans = self.a[r]
            r -= 1
            while r - (r & -r) >= l:
                # ans = max(self.h[r], ans)
                if ans < self.h[r]:
                    ans = self.h[r]
                r -= (r & -r)
        return ans

    def lowbit(self, x):
        return x & -x


"""
单调栈求出每个值作为最小值的管辖范围，
假设值x范围长度是k，那么显然[1~k]长度的区间它都能生成，即f(1~k)都可以用x更新；
反过来讲：对f(i)来说，管辖>=i的x都可以用来更新f(i)

那么就是求一个区间最大值的问题。可以用树状数组/线段树
也可以排序双指针，但是要逆序且记录max
by灵神：只需要更新每个管辖范围i对f(i)的答案，然后倒着推一遍f即可，即求后缀最大值
"""


#   421  ms 只更新单点答案，然后倒着推f，求后缀最大值
def solve():
    n, = RI()
    a = RILST()
    ms = MonoStack(a)
    ls, rs = ms.get_true_bound_as_min()  # 单调栈求每个位置作为最小值能管辖到的左右边界

    ans = [0] * n
    for l, r, x in zip(ls, rs, a):
        p = r - l - 1 - 1
        if ans[p] < x:
            ans[p] = x

    for i in range(n-2, -1, -1):
        if ans[i] < ans[i+1]:
            ans[i] = ans[i+1]

    print(*ans)

#   467  ms 只更新单点答案，然后倒着推f，求后缀最大值
def solve4():
    n, = RI()
    a = RILST()
    ms = MonoStack(a)
    ls, rs = ms.get_true_bound_as_min()  # 单调栈求每个位置作为最小值能管辖到的左右边界

    ans = [0] * (n + 1)
    for l, r, x in zip(ls, rs, a):
        p = r - l - 1
        if ans[p] < x:
            ans[p] = x

    for i in range(n-1, 0, -1):
        if ans[i] < ans[i+1]:
            ans[i] = ans[i+1]

    print(*ans[1:])


#   998  ms/TLE10
def solve3():
    n, = RI()
    a = RILST()
    ms = MonoStack(a)
    ls, rs = ms.get_true_bound_as_min()  # 单调栈求每个位置作为最小值能管辖到的左右边界

    c = []
    for l, r, x in zip(ls, rs, a):
        p = r - l - 1
        c.append((p, x))  # 管辖范围，值  这里写[p,x]就TLE
    c.sort()

    j = len(c) - 1
    ans = [0] * n
    mx = 0
    for i in range(n, 0, -1):
        while j >= 0 and c[j][0] >= i:
            # mx = max(mx, c[j][1])
            if mx < c[j][1]:
                mx = c[j][1]
            j -= 1
        ans[i - 1] = mx

    print(*ans)


#   499   ms
def solve2():
    n, = RI()
    a = RILST()
    ms = MonoStack(a)
    ls, rs = ms.get_true_bound_as_min()  # 单调栈求每个位置作为最小值能管辖到的左右边界

    ctrl = {}
    for l, r, x in zip(ls, rs, a):
        p = r - l - 1
        ctrl[p] = max(ctrl.get(p, x), x)
    c = sorted([(k, v) for k, v in ctrl.items()])

    j = len(c) - 1
    ans = [0] * n
    mx = 0
    for i in range(n, 0, -1):
        while j >= 0 and c[j][0] >= i:
            mx = max(mx, c[j][1])
            j -= 1
        ans[i - 1] = mx

    print(*ans)


#   701    ms
def solve1():
    n, = RI()
    a = RILST()
    ms = MonoStack(a)
    ls, rs = ms.get_true_bound_as_min()  # 单调栈求每个位置作为最小值能管辖到的左右边界
    tree = BinIndexTreeMax(n + 1)  # 树状数组记录每个管辖范围对应的最大数
    mx = [0] * (n + 1)  # 每个位置只记最大值
    for l, r, x in zip(ls, rs, a):
        p = r - l - 1
        mx[p] = max(mx[p], x)
        tree.set_point(p, mx[p])
    ans = []
    for i in range(1, n + 1):
        ans.append(tree.query_interval_max(i, n))  # f(x) = max(tree[i~n])：即管辖范围超过x，这个值就可以更新f(x)的答案
    print(*ans)


if __name__ == '__main__':
    solve()

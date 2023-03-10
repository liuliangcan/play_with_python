# Problem: D. Max GEQ Sum
# Contest: Codeforces - CodeCraft-22 and Codeforces Round #795 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1691/D
# Memory Limit: 256 MB
# Time Limit: 1500 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1691/D

输入 t(≤1e5) 表示 t 组数据，每组数据输入 n(≤2e5) 和长为 n 的数组 a (-1e9≤a[i]≤1e9)。所有数据的 n 之和不超过 2e5。

请你判断，对数组 a 的每个非空子数组 b，是否都有 max(b) >= sum(b)？
如果是，输出 YES，否则输出 NO。
注：子数组是连续的。

进阶：做到 O(n) 时间复杂度。
输入
3
4
-1 1 -1 2
5
-1 2 -3 2 -1
3
2 3 -1
输入
YES
YES
NO
解释 对于第三组数据，子数组 b=[2,3] 是不满足的。
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


class SparseTable:
    def __init__(self, data: list, func=max):
        # 稀疏表，O(nlgn)预处理，O(1)查询区间最值/或和/gcd/lcm
        # 下标从0开始
        self.func = func
        self.st = st = [list(data)]
        i, N = 1, len(st[0])
        while 2 * i <= N + 1:
            pre = st[-1]
            st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1

    def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
        lg = (end - begin + 1).bit_length() - 1
        return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])


"""https://codeforces.com/contest/1691/submission/189346222

提示 1：看到子数组+min/max，就要想单调栈。
对于本题，假设把 a[i] 当作最大值，那么需要得到能把 a[i] 当作最大值的区间左端点的最小值 L，和右端点的最大值 R。这就需要单调栈了。

提示 2：用前缀和思考。
需要在 L 到 i 之间选一个最小的前缀和，i 到 R 之间选一个最大的前缀和。这样子数组和才最大。
如果子数组和 > a[i]，那么输出 NO。
这可以用 ST 表或者线段树实现。

还有更快的做法吗？

提示 3：继续研究，如果从 i-1 向左走，累加元素和，会得到一个 >0 的元素和的话，那么它 + a[i] > a[i]，就要输出 NO 了。
可以在单调栈出栈的时候，去判断是否有这样的情况。
为什么只需要考虑单调栈的元素？
因为其他的下标已经被之前的元素弹出去了，这个下标到 i-1 的元素和必然是 <= 0 的。
对于从 i+1 向右走的情况也一样，倒序单调栈的同时去判断。

不在单调栈里的元素，为什么不用考虑?
一定是提前被弹出去了，假设是j，需要考虑sum[j,i-1]吗？
设j被k弹出去了，且没return False,那么sum[j,k-1]一定<=0,那么
    sum[j,i-1] = sum[j,k-1] + sum[k,i-1] <= sum[k,i-1]
    即 sum[j,i-1]<= sum[k,i-1]
    显然若后一段<=0则前一段必<=0
    因此只考虑sum[k,i-1]即可
"""


class ZKW:
    # n = 1
    # size = 1
    # log = 2
    # d = [0]
    # op = None
    # e = 10 ** 15
    """自低向上非递归写法线段树，0_indexed
    tmx = ZKW(pre, max, -2 ** 61)
    """
    __slots__ = ('n', 'op', 'e', 'log', 'size', 'd')

    def __init__(self, V, OP, E):
        """
        V: 原数组
        OP: 操作:max,min,sum
        E: 每个元素默认值
        """
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p and p < self.n
        update = self.update
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        # assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def query(self, l, r):  # [l,r)左闭右开
        # assert 0 <= l and l <= r and r <= self.n
        sml, smr, op, d = self.e, self.e, self.op, self.d

        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_query(self):
        return self.d[1]

    def max_right(self, l, f):
        """返回l右侧第一个不满足f的位置"""
        # assert 0 <= l and l <= self.n
        # assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size

        sm, op, d, size = self.e, self.op, self.d, self.size
        while True:
            while l % 2 == 0:
                l >>= 1
            if not (f(op(sm, d[l]))):
                while l < size:
                    l = 2 * l
                    if f(op(sm, d[l])):
                        sm = op(sm, d[l])
                        l += 1
                return l - size
            sm = op(sm, d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """返回r左侧连续满足f的最远位置的位置"""
        # assert 0 <= r and r < self.n
        # assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm, op, d, size = self.e, self.op, self.d, self.size

        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (f(op(d[r], sm))):
                while r < size:
                    r = (2 * r + 1)
                    if f(op(d[r], sm)):
                        sm = op(d[r], sm)
                        r -= 1
                return r + 1 - size
            sm = op(d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


#  783  ms
def solve():
    n, = RI()
    a = [0] + RILST()
    sot = [(a[i], i) for i in range(1, n + 1)]
    sot.sort(reverse=True, key=lambda x: x[0])
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    ind = ZKW([0] * (n + 3), lambda x, y: max(x, y), 0)
    ind.set(0, 1)
    ind.set(n + 1, 1)
    smin = ZKW(s, lambda x, y: min(x, y), 2 ** 61)
    smax = ZKW(s, lambda x, y: max(x, y), -2 ** 61)
    ans = "YES"
    for num, i in sot:
        def f(x):
            return x == 0

        l = ind.min_left(i, f)
        r = ind.max_right(i, f) - 1

        sq = smax.query(i, r + 1)
        sp1 = smin.query(l - 1, i)
        if num < sq - sp1: ans = "NO"
        ind.set(i, 1)

    print(ans)


#  374  ms
def solve5():
    n, = RI()
    a = RILST()
    l = [-1] * n
    for i in range(n):
        j = i - 1
        while j != -1 and a[j] <= a[i]:
            j = l[j]
        l[i] = j
    r = [n] * n
    for i in range(n - 1, -1, -1):
        j = i + 1
        while j != n and a[j] <= a[i]:
            j = r[j]
        r[i] = j
    pre = [0] + list(accumulate(a))
    tmx = ZKW(pre, max, -2 ** 61)
    tmn = ZKW(pre, min, 2 ** 61)
    for i, (x, y) in enumerate(zip(l, r)):
        x += 1
        y -= 1
        mx = tmx.query(i + 1, y + 2)
        mn = tmn.query(x, i + 1)
        if a[i] < mx - mn:
            return print('NO')
    print('YES')


#  374  ms
def solve4():
    n, = RI()
    a = RILST()
    l = [-1] * n
    for i in range(n):
        j = i - 1
        while j != -1 and a[j] <= a[i]:
            j = l[j]
        l[i] = j
    r = [n] * n
    for i in range(n - 1, -1, -1):
        j = i + 1
        while j != n and a[j] <= a[i]:
            j = r[j]
        r[i] = j
    pre = [0] + list(accumulate(a))
    stmx = SparseTable(pre, max)
    stmn = SparseTable(pre, min)
    for i, (x, y) in enumerate(zip(l, r)):
        x += 1
        y -= 1
        mx = stmx.query(i + 1, y + 1)
        mn = stmn.query(x, i)
        if a[i] < mx - mn:
            return print('NO')
    print('YES')


#   202 ms
def solve3():
    n, = RI()
    a = RILST()

    def f(a):
        st, g, s = [], [], 0  # 单调栈，前缀和
        for v in a:
            while st and st[-1] <= v:
                if g[-1] < s:  # 弹出的数都在管辖范围内,其中若有一个小于s的前缀和,说明这俩会计算出一个正子段
                    return False  # 一个正子段和最大值相邻，寄
                st.pop()
                g.pop()
            st.append(v)
            g.append(s)
            s += v
        return True

    print('YES' if f(a) and f(a[::-1]) else 'NO')


#   311 ms
def solve2():
    n, = RI()
    a = RILST()

    def f(a):
        st, s = [], 0  # 单调栈，前缀和
        for v in a:
            while st and st[-1][0] <= v:
                if st[-1][1] < s:  # 弹出的数都在管辖范围内,其中若有一个小于s的前缀和,说明这俩会计算出一个正子段
                    return False  # 一个正子段和最大值相邻，寄
                st.pop()
            st.append((v, s))
            s += v
        return True

    print('YES' if f(a) and f(a[::-1]) else 'NO')


#   374 ms
def solve1():
    n, = RI()
    a = RILST()
    l, r = MonoStack(a).get_true_bound_as_max()
    pre = [0] + list(accumulate(a))
    stmx = SparseTable(pre, max)
    stmn = SparseTable(pre, min)
    for i, (x, y) in enumerate(zip(l, r)):
        x += 1
        y -= 1
        mx = stmx.query(i + 1, y + 1)
        mn = stmn.query(x, i)
        if a[i] < mx - mn:
            return print('NO')

    print('YES')


if __name__ == '__main__':
    t, = RI()  # t, = RI()
    for _ in range(t):
        solve()

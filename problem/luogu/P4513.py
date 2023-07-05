# Problem: P4513 小白逛公园
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P4513
# Memory Limit: 128 MB
# Time Limit: 1000 ms

import sys
from math import inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

PROBLEM = """在线询问区间最大子段和。
4棵线段树。每个节点储存当前区间最大子段和、当前区间和、当前区间包含左边界的最大子段和(最大前缀和)、当前区间包含右边界的最大子段和(最大后缀和)
py使用zkw+快读快写可以过
"""


class IntervalTree:
    """区间加，区间求和"""

    def __init__(self, size, a=None):
        self.size = size
        self.ms = [0 for _ in range(size * 4)]
        self.s = [0 for _ in range(size * 4)]
        self.ls = [0 for _ in range(size * 4)]
        self.rs = [0 for _ in range(size * 4)]
        if a:
            self.a = a
            self.build(1, 1, size)

    def update_by_son(self, p, l, r):
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        x, y = p << 1, p << 1 | 1
        ms[p] = max(ms[x], ms[y], ls[y] + rs[x])
        s[p] = s[x] + s[y]
        ls[p] = max(s[x] + ls[y], ls[x])
        rs[p] = max(s[y] + rs[x], rs[y])

    def build(self, p, l, r):
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        if l == r:
            ms[p] = s[p] = ls[p] = rs[p] = self.a[l - 1]
            return
        mid = (l + r) >> 1
        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)
        self.update_by_son(p, l, r)

    def update_point(self, p, l, r, x, val):
        """
        把x位置变成val
        """
        if x < l or r < x:
            return
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        if l == r:
            ms[p] = s[p] = ls[p] = rs[p] = val
            return

        mid = (l + r) // 2

        if x <= mid:
            self.update_point(p << 1, l, mid, x, val)
        if mid < x:
            self.update_point(p << 1 | 1, mid + 1, r, x, val)
        self.update_by_son(p, l, r)

    def query_interval(self, p, l, r, x, y):
        """
        查找x,y区间的最大子段和        """

        # if y < l or r < x:
        #     return -inf, 0, -inf, -inf
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        if x <= l and r <= y:
            return ms[p], s[p], ls[p], rs[p]

        mid = (l + r) >> 1
        a1, a2, a3, a4 = -inf, 0, -inf, -inf
        b1, b2, b3, b4 = -inf, 0, -inf, -inf
        # if x <= mid < y:
        #     a1, a2, a3, a4 = self.query_interval(p << 1, l, mid, x, y)
        #     b1, b2, b3, b4 = self.query_interval(p << 1 | 1, mid + 1, r, x, y)
        #     return max(a1, b1, b3 + a4), a2 + b2, max(a3, a2 + b3), max(b4, b2 + a4)

        if x <= mid:
            a1, a2, a3, a4 = self.query_interval(p << 1, l, mid, x, y)
        if mid < y:
            b1, b2, b3, b4 = self.query_interval(p << 1 | 1, mid + 1, r, x, y)
        return max(a1, b1, b3 + a4), a2 + b2, max(a3, a2 + b3), max(b4, b2 + a4)


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

    # __slots__ = ('n', 'op', 'e', 'log', 'size', 'd')

    def __init__(self, V):
        """
        V: 原数组
        OP: 操作:max,min,sum
        E: 每个元素默认值
        """
        self.n = len(V)
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.ms = [0 for i in range(2 * self.size)]
        self.s = [0 for i in range(2 * self.size)]
        self.ls = [0 for i in range(2 * self.size)]
        self.rs = [0 for i in range(2 * self.size)]
        # ms = self.ms = [0] * (2 * self.size)
        # s = self.s = [0] * (2 * self.size)
        # ls = self.ls = [0] * (2 * self.size)
        # rs = self.rs = [0] * (2 * self.size)
        for i in range(self.n):
            self.ms[self.size + i] = self.s[self.size + i] = self.ls[self.size + i] = self.rs[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p and p < self.n
        update = self.update
        p += self.size
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        ms[p] = s[p] = ls[p] = rs[p] = x
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        # assert 0 <= p and p < self.n
        return self.s[p + self.size]

    def query(self, l, r):  # [l,r)左闭右开
        # assert 0 <= l and l <= r and r <= self.n
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        l += self.size
        r += self.size

        a1, a2, a3, a4 = -inf, 0, -inf, -inf
        b1, b2, b3, b4 = -inf, 0, -inf, -inf
        while l < r:
            if l & 1:
                a1, a2, a3, a4 = max(a1, ms[l], ls[l] + a4), a2 + s[l], max(a3, a2 + ls[l]), max(rs[l], s[l] + a4)
                l += 1
            if r & 1:
                b1, b2, b3, b4 = max(ms[r - 1], b1, b3 + rs[r - 1]), s[r - 1] + b2, max(ls[r - 1], s[r - 1] + b3), max(
                    b4, b2 + rs[r - 1])
                r -= 1
            l >>= 1
            r >>= 1
        return max(a1, b1, b3 + a4), a2 + b2, max(a3, a2 + b3), max(b4, b2 + a4)

    def update(self, p):
        ms, s, ls, rs = self.ms, self.s, self.ls, self.rs
        # self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])
        x, y = p << 1, p << 1 | 1
        ms[p] = max(ms[x], ms[y], ls[y] + rs[x])
        s[p] = s[x] + s[y]
        ls[p] = max(s[x] + ls[y], ls[x])
        rs[p] = max(s[y] + rs[x], rs[y])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


#    必须开快写 979  ms
def solve():
    n, m = RI()
    a = []
    for _ in range(n):
        v, = RI()
        a.append(v)

    tree = ZKW(a)
    for _ in range(m):
        t, a, b = RI()
        if t == 1:
            if a > b:
                a, b = b, a
            print(tree.query(a - 1, b)[0])
        else:
            tree.set(a - 1, b)


#     TLE+MLE  ms
def solve1():
    n, m = RI()
    a = []
    for _ in range(n):
        v, = RI()
        a.append(v)

    tree = IntervalTree(n, a)
    for _ in range(m):
        t, a, b = RI()
        if t == 1:
            if a > b:
                a, b = b, a
            print(tree.query_interval(1, 1, n, a, b)[0])
        else:
            tree.update_point(1, 1, n, a, b)


solve()

# Problem: F - Christmas Present 2
# Contest: AtCoder - UNIQUE VISION Programming Contest 2023 Christmas (AtCoder Beginner Contest 334)
# URL: https://atcoder.jp/contests/abc334/tasks/abc334_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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


#       ms
def solve():
    n, k = RI()
    a = []
    sx, sy = RI()
    for _ in range(n):
        x, y = RI()
        a.append((x - sx, y - sy))

    def dis(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    d0 = [dis(x, y, 0, 0) for x, y in a]
    p = []
    for i in range(1, n):
        p.append(dis(a[i][0], a[i][1], a[i - 1][0], a[i - 1][1]))

    pred0 = [0] + list(accumulate(p))
    f = [inf] * (n + 1)  # f[i+1] 表示到i位置返回房子的最小距离
    f[0] = 0
    c = [inf] * (n + 1)

    def add(i, v):
        while i <= n:
            c[i] = min(c[i], v)
            i += i & -i

    def get(i):
        s = inf
        while i:
            s = min(s, c[i])
            i -= i & -i
        return s

    for i in range(n):
        add(n - i, f[i] - pred0[i] + d0[i])
        f[i + 1] = get(n - max(-1, i - k) - 1) + pred0[i] + d0[i]

    print(f[-1])


#       ms
def solve1():
    n, k = RI()
    a = []
    sx, sy = RI()
    for _ in range(n):
        x, y = RI()
        a.append((x - sx, y - sy))

    def dis(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    d0 = [dis(x, y, 0, 0) for x, y in a]
    p = []
    for i in range(1, n):
        p.append(dis(a[i][0], a[i][1], a[i - 1][0], a[i - 1][1]))

    pred0 = [0] + list(accumulate(p))
    f = [inf] * (n + 1)  # f[i+1] 表示到i位置返回房子的最小距离
    f[0] = 0
    zkw = ZKW([inf] * n, min, inf)
    for i in range(n):
        zkw.set(i, f[i] - pred0[i] + d0[i])
        f[i + 1] = zkw.query(max(-1, i - k) + 1, i + 1) + pred0[i] + d0[i]

        # for j in range(i,max(-1,i-k),-1):
        #
        #     f[i+1] = min(f[i+1], f[j]-pred0[j]+d0[j]  +pred0[i] +d0[i])
    # print(f)
    # print(zkw)
    print(f[-1])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

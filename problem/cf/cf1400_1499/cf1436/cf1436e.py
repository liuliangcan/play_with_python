# Problem: E. Complicated Computations
# Contest: Codeforces - Codeforces Round 678 (Div. 2)
# URL: https://codeforces.com/contest/1436/problem/E
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/1436/problem/E

输入 n(1≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤n)。

定义一个数组的 mex 为不在这个数组中的最小正整数。
把 a 的所有非空连续子数组的 mex 丢到一个数组 b 中，输出 b 的 mex。
输入
3
1 3 2
输出 3

输入
5
1 4 3 1 2
输出 6
"""
"""把所有可能的子数组 mex 算出来，就可以算出答案。

例如，要检查是否有子数组的 mex 等于 6，我们可以把 a 按照 6 切分成若干段，检查是否有一段包含了 [1,5] 中的所有整数。如果包含，那么这一段的 mex 就是 6。

我们可以在遍历 a 的同时，维护每个 a[i] 最近一次出现的下标，以及用一棵值域线段树维护元素的最小下标。
对于 a[i] 来说，用线段树计算 1 到 a[i]-1 中的每个数的最近一次出现下标的最小值（记作 minIdx），如果 minIdx 大于上一个 a[i] 的出现位置，就说明这两个 a[i] 之间，包含了 1 到 a[i]-1 中的所有整数，那么这一段（两个 a[i] 之间）的 mex 等于 a[i]。

其它情况：
如果 a 中有 1，那么子数组的 mex 可以等于 2。
如果 a 中有大于 1 的数，那么子数组的 mex 可以等于 1。

https://codeforces.com/problemset/submission/1436/249298385"""


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
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


#       ms
def solve():
    n, = RI()
    a = RILST()
    zkw = ZKW([-1] * (n + 1), min, n)
    prei = [-1] * (n + 2)
    ans = [False] * (n + 3)

    for i, v in enumerate(a):
        if v == 1:
            ans[2] = True
        else:
            ans[1] = True

            if zkw.query(1, v) > prei[v]:
                ans[v] = True
        zkw.set(v, i)
        prei[v] = i

    for v in range(2, n + 2):
        if not ans[v] and zkw.query(1, v) > prei[v]:
            ans[v] = True

    # s = set(a)
    # mex = 1
    # while mex in s:
    #     mex += 1
    # ans[mex] = True
    mex = 1
    while ans[mex]:
        mex += 1

    print(mex)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

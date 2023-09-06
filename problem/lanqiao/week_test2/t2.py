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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


class BinTree2DIUPQ:
    """二维树状数组"""

    def __init__(self, m, n):
        self.n = n
        self.m = m
        self.tree = [[0] * (n + 1) for _ in range(m + 1)]

    def lowbit(self, x):
        return x & (-x)

    def _update_point(self, x, y, val):
        m, n, tree = self.m, self.n, self.tree
        while x <= m:
            y1 = y
            while y1 <= n:
                tree[x][y1] += val
                y1 += y1 & -y1
            x += x & -x

    def _sum_prefix(self, x, y):
        res = 0
        tree = self.tree
        while x > 0:
            y1 = y
            while y1 > 0:
                res += tree[x][y1]
                y1 &= y1 - 1
            x &= x - 1
        return res

    def add_interval(self, x1, y1, x2, y2, v):
        self._update_point(x1, y1, v)
        self._update_point(x2 + 1, y1, -v)
        self._update_point(x1, y2 + 1, -v)
        self._update_point(x2 + 1, y2 + 1, v)

    def query_point(self, x, y):
        return self._sum_prefix(x, y)


#       ms
def solve():
    n, m, q = RI()
    tree = BinTree2DIUPQ(n, m)

    for i in range(1, n + 1):
        row = RILST()
        for j, v in enumerate(row, start=1):
            tree.add_interval(i, j, i, j, v)
    for _ in range(q):
        x1, y1, x2, y2, c = RI()
        tree.add_interval(x1, y1, x2, y2, c)

    for i in range(1, n + 1):
        ans = []
        for j in range(1, m + 1):
            ans.append(tree.query_point(i, j))
        print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

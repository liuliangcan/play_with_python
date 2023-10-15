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


#    1887   ms
def solve():
    n, m = RI()
    s, = RS()
    k = max(2, int(sqrt(n)))  # 分块宽度
    bit = BinIndexTreeRUPQ(n)
    for i, c in enumerate(s, start=1):
        bit.add_interval(i, i, ord(c) - ord('a'))

    def check_one(l, r):  # 检查这小段是否合法，保证长度小，可以暴力
        x, y = -1, -2
        for i in range(l, r + 1):
            z = bit.query_point(i)
            if z == x or z == y:
                return False
            x, y = y, z
        return True

    def check(l, r):  # 查询[l,r]是否合法，不保证长度小
        if r - l <= k:
            return check_one(l, r)
        p1, p2 = (l - 1) // k, (r - 1) // k
        for i in range(p1 + 1, p2):  # 内含的完整块有不合法的就不行
            if not fen[i]:
                return False
        if not check_one(l, min(r, fenk[p1 + 1][0] + 1)):  # 第一段，顺便连上第二块的前俩位置
            return False
        if not check_one(max(l, fenk[p2 - 1][1] - 1), r):  # 最后一段，顺便连倒数第二块的后俩位置
            return False
        for i in range(p1 + 1, p2 - 1):  # 中间完整块，讨论边界的4块。
            if not check_one(max(l, fenk[i][1] - 1), min(r, fenk[i + 1][0] + 1)):
                return False
        return True

    fenk = [(i + 1, min(i + k, n)) for i in range(0, n, k)]
    fen = [check_one(l, r) for l, r in fenk]

    for _ in range(m):
        t, *ops = RI()
        if t == 1:
            l, r, x = ops
            bit.add_interval(l, r, x)  # 用bit来RUPQ，取模26即可
            for p in (l - 1) // k, (r - 1) // k:  # 只需要更新首尾所在的两个段，其余段不变
                fen[p] = check_one(*fenk[p])
        else:
            l, r = ops
            print(['NO', 'YES'][check(l, r)])


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
